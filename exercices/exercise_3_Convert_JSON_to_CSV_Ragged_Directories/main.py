''' Run ragged dirs and convert JSON files to CSV  '''

import glob
import os
import csv
import json 

# Convert
def convert_to_csv(file) -> None:
    with open(file, 'r') as f:
        j_data = json.load(f)

    # Verify the json is a list of dicts, common when converting to CSV
    if isinstance(j_data, list) and all(isinstance(item, dict) for item in j_data):  
       
       csv_files_dir = create_csv_dir()

       csv_file_base_name = os.path.splitext(os.path.basename(json_file))[0]
       csv_file = os.path.join(csv_files_dir, "{}.csv".format(csv_file_base_name))

       # Write to csv
       with open(csv_file, 'w+', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=j_data[0].keys())
            writer.writeheader()
            writer.writerows(j_data)            
            print("Json file converted to csv. {}. CSV files saved on new directory.".format(csv_file))           

    else:
       print("Unspected format in {}, convertion was not possible.".format(file))


# AUX function:
def create_csv_dir()-> None:
    csv_files_dir = 'csv_files_dir'

    if not os.path.exists(csv_files_dir):
        os.makedirs(csv_files_dir)    
    return csv_files_dir


# Finding json files inside any directory:
def _get_json_files()->list:
    json_files = glob.glob('**/*.json', recursive=True)
    return json_files  


for json_file in _get_json_files():
    convert_to_csv(json_file)