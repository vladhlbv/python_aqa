import urllib.request
import json
import xmltodict

from lesson_13.file_logger import file_logger
from lesson_13.console_logger import console_logger


def get_file_from_repo (raw_file_url: str, file_path: str) -> None:
    """
    Function retrieves necessary file with provided raw URL and saves it to the provided location.
    :param raw_file_url: Raw URL of the necessary file for retrieval
    :param file_path:  Location and name of downloaded file
    """
    urllib.request.urlretrieve(raw_file_url,file_path)


def validate_json (file_path: str) -> None:
    """
    Function validates json file that is provided and writes result in log if file was successfully validated or not.
    :param file_path: File path to the necessary json file
    """
    log_message_success = f"File: {file_path} successfully validated"
    log_message_error = f"File: {file_path} validated with errors:"

    try:
        try:
            with open(file_path, 'r') as jsonfile:
                json_string = json.load(jsonfile)
            file_logger.info(log_message_success)
        except UnicodeDecodeError as e:
            file_logger.error(log_message_error, exc_info = True)
    except json.JSONDecodeError as e:
        file_logger.error(log_message_error, exc_info = True)


def get_incoming_by_group_number (group_number: str) -> None:
    """
    Function outputs value of Incoming bytes by input value of Group number.
    :param group_number: value of Group number by which the search should be conducted
    """
    with (open("files/xml_downloaded_1.xml", 'r') as file):
        xml_string: str = file.read()
        xml_converted: dict = xmltodict.parse(xml_string)

    incoming_number: list = [group_data.get("timingExbytes").get("incoming") for group_data in
                             xml_converted["groups"]["group"] if group_data.get("number") == group_number]

    incoming_number_str: str = incoming_number[0]

    console_logger.info(f"Incoming number: {incoming_number_str} for group number: {group_number}")