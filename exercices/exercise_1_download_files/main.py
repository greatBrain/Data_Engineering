import requests as rq

download_uris = [   
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip"
]

def get_dir() -> str:
    down_dir = 'download'
    dir_exists = os.path.exists(down_dir)

    if not dir_exists:        
       os.makedirs(down_dir)      
    return down_dir


def download() -> str:
    file_num = 1
    dir = get_dir()

    while True:
        for item in range(len(download_uris)):
            result = rq.get(download_uris[item], allow_redirects=True)
            open('{}/trip_data_dataset{}.zip'.format(dir, file_num), 'wb').write(result.content)
            file_num +=1
        break
    return "File downloading ready!"

def run() -> None:
    download()

if __name__ == "__main__":
    run() 
