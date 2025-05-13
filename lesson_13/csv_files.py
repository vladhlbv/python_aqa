import csv
from lesson_13.file_operations import get_file_from_repo

urls_csv: list[str] = ["https://raw.githubusercontent.com/dntpanix/automation_qa/refs/heads/main/ideas_for_test/work_with_csv/r-m-c.csv", "https://raw.githubusercontent.com/dntpanix/automation_qa/refs/heads/main/ideas_for_test/work_with_csv/random.csv"]
csv_file_paths: list[str] = ["files/csv_downloaded_1.csv", "files/csv_downloaded_2.csv"]


# Download necessary files from the remote repository
get_file_from_repo(raw_file_url=urls_csv[0], file_path=csv_file_paths[0])
get_file_from_repo(raw_file_url=urls_csv[1], file_path=csv_file_paths[1])


csv_values: list = []

# Read first new csv file and write it to the list
with open(csv_file_paths[0], 'r') as csvfile:
    for line in csvfile:
        columns = line.strip().split(',')
        if columns not in csv_values:
            csv_values.append(columns)


# Read second new csv file and write it to the list if values are unique
with open(csv_file_paths[1], 'r') as csvfile:
    for line in csvfile:
        columns = line.strip().split(',')
        if columns not in csv_values:
            csv_values.append(columns)


# Write new csv file with unique values
with open('files/csv_output.csv', 'w', newline="") as out_file:
    writer = csv.writer(out_file)
    writer.writerows(csv_values)