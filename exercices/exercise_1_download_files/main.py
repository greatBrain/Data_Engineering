import requests as rq
import os
from zipfile import ZipFile

download_uris = [   
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
]

def get_dir() -> str:
    down_dir = 'download'

    if not os.path.exists(down_dir):
       os.makedirs(down_dir)      
    return down_dir

def download()-> None:
    dir = get_dir()

    while True:
        for item in range(len(download_uris)):
            result = rq.get(download_uris[item], allow_redirects=True)
            file_name = download_uris[item].split('/')[-1]
            open('{}/{}'.format(dir, file_name), 'wb').write(result.content)
        break

    print("File downloading ready...", "\n", "Unzipping files:")
    unzip_files_in_dir(dir)


def unzip_files_in_dir(dir:str) -> None:   
    zip_files = [file for file in os.listdir(dir) if file.endswith('.zip')]

    if not zip_files:
       print("No .zip files for unzip...") 

    for file in zip_files:
        file_path = os.path.join(dir, file)

        try:
            with ZipFile(file_path, "r") as zip_file_rpr:
                 print("Extracting.... Please wait.")
                 zip_file_rpr.extractall(dir)
                 delete_zip_files(dir)
            print("files extracted sucessfully!")

        except Exception as e:
            print("Error unzipping {}, {}".format(file, e))


def delete_zip_files(dir:str):
    files = os.listdir(dir)

    for file in files:
        if not file.endswith('.csv'):
           file_path = os.path.join(dir, file)
           os.remove(file_path)
    print("zip files removed!")


def run() -> None:
    download()

if __name__ == "__main__":
    run() 
