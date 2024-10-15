import requests as rq
import os
from zipfile import ZipFile

class Downloader:
      def __init__(self):
          self.download_uris = [
              "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
              "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
              "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
              "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
              "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
              "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
          ]

          self.down_dir = 'download'

      def get_dir(self) -> str:
          self.down_dir

          if not os.path.exists(self.down_dir):
             os.makedirs(self.down_dir)
          return self.down_dir


      def download(self) -> None:
          dir = self.get_dir()

          while True:
              for item in range(len(self.download_uris)):
                  result = rq.get(self.download_uris[item], allow_redirects=True)
                  file_name = self.download_uris[item].split('/')[-1]
                  open('{}/{}'.format(dir, file_name), 'wb').write(result.content)
              break

          print("File downloading ready...", "\n", "Unzipping files:")
          self.unzip_files_in_dir(dir)


      def unzip_files_in_dir(self, dir:str) -> None:
          zip_files = [file for file in os.listdir(dir) if file.endswith('.zip')]

          if not zip_files:
             print("No .zip files for unzip...")

          for file in zip_files:
              file_path = os.path.join(dir, file)

              try:
                  with ZipFile(file_path, "r") as zip_file_rpr:
                       print("Extracting.... Please wait.")
                       zip_file_rpr.extractall(dir)
                       self.delete_zip_files(dir)
                  print("files extracted sucessfully!")
              except Exception as e:
                  print("Error unzipping {}, {}".format(file, e))


      def delete_zip_files(self, dir:str):
           files = os.listdir(dir)

           for file in files:
               if not file.endswith('.csv'):
                  file_path = os.path.join(dir, file)
                  os.remove(file_path)
           print("zip files removed!")


      def run(self) -> None:
          self.download()

if __name__ == "__main__":
   downloader = Downloader()
   downloader.run()
