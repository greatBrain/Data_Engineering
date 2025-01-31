# Biodiversity DAG for pipeline purpose

from airflow import DAG
from datetime import datetime
from airflow.decorators import task, dag
import requests as rq
import json

# DAG definition

default_args = {
    'owner':'airflow',
    'start_date':datetime.now(),
    'catchup':False
}

@dag(
    dag_id = "biodiversity_pipeline",
    default_args = default_args,
    schedule_interval='@daily',
    description='For the preservation of the biodiversity data pipeline',
    tags=['biodiversity', 'sqlite', 'datapipeline', 'biology', 'science']
)

def bio_pipeline():
    """ Extract data from the API  """
    
    @task(retries=3)
    def extract_data():
        endpoint_url = "https://api.gbif.org/v1/occurrence/search"
        
        params = {
            "hashasCoordinate":"true",
            "limit":100
        }        
        response = rq.get(endpoint_url, params=params)        
        
        if not response.status_code==200:
           raise response.Exception("Error fetching the data. {}".format(response.status_code))
        
        data = response.json()
        return data["results"]
    
    @task()
    def transform_data(raw_data:list) -> list:
        _filtered_data=[
            {
                "scientificName":record.get("scientificName"),
                "latitude": record["decimalLatitude"],
                "longitude": record["decimalLongitude"],
                "eventDate": record["eventDate"],
                "country": record.get("country") or "Unknown"
            }
            for record in raw_data 
            if all(record.get(key) for key in ["scientificName", "latitude", "longitude", "eventDate", "country"])
        ]
        return _filtered_data
    
bio_pipeline()
