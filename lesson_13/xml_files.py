from lesson_13.file_operations import get_file_from_repo
from lesson_13.file_operations import get_incoming_by_group_number

url_xml: str = "https://raw.githubusercontent.com/dntpanix/automation_qa/refs/heads/main/ideas_for_test/work_with_xml/groups.xml"
xml_file_path: str = "files/xml_downloaded_1.xml"


# Download necessary files from the remote repository
get_file_from_repo(raw_file_url=url_xml, file_path=xml_file_path)


# Search in downloaded XML document by group number
get_incoming_by_group_number(group_number='0')