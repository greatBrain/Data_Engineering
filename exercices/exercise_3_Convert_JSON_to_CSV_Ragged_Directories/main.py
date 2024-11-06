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

       # Defining the csv file name:
       csv_file = os.path.splitext(file)[0] + '.csv'

       # Write to csv
       with open(csv_file, 'w+', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=j_data[0].keys())
            writer.writeheader()
            writer.writerows(j_data)
            
            print("Json file converted to csv. {}".format(csv_file))

    else:
       print("Unspected format in {}, convertion was not possible.".format(file))


# Finding json files inside any directory:
def get_json_files()->list:
    json_files = glob.glob('**/*.json', recursive=True)
    return json_files
  

for json_file in get_json_files():
    convert_to_csv(json_file)