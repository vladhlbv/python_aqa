import json
from lesson_13.file_operations import get_file_from_repo
from lesson_13.file_operations import validate_json

urls_json: list[str] = ["https://raw.githubusercontent.com/dntpanix/automation_qa/refs/heads/main/ideas_for_test/work_with_json/localizations_en.json", "https://raw.githubusercontent.com/dntpanix/automation_qa/refs/heads/main/ideas_for_test/work_with_json/localizations_ru.json", "https://raw.githubusercontent.com/dntpanix/automation_qa/refs/heads/main/ideas_for_test/work_with_json/login.json", "https://raw.githubusercontent.com/dntpanix/automation_qa/refs/heads/main/ideas_for_test/work_with_json/swagger.json"]
json_file_paths: list[str] = ["files/json_downloaded_1.json", "files/json_downloaded_2.json", "files/json_downloaded_3.json", "files/json_downloaded_4.json"]


# Download necessary files from the remote repository
get_file_from_repo(raw_file_url= urls_json[0], file_path=json_file_paths[0])
get_file_from_repo(raw_file_url= urls_json[1], file_path=json_file_paths[1])
get_file_from_repo(raw_file_url= urls_json[2], file_path=json_file_paths[2])
get_file_from_repo(raw_file_url= urls_json[3], file_path=json_file_paths[3])


# Validate files from json_file_paths list
for value in json_file_paths:
    validate_json(value)