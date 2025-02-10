import csv
import json
import os

def create_csv(file_path, file_name):
    carpeta_uploads = os.path.dirname(file_path)
    file_name_omit_extension = file_name.replace(".json", "")
 
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    dir_path_csv = os.path.join(carpeta_uploads, f"{file_name_omit_extension}.csv")
    with open(dir_path_csv, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(data[0].keys())

        for item in data:
            writer.writerow(item.values())
    return dir_path_csv