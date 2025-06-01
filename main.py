from src.connection import get_json_from_url , get_data_csv
import json
import requests
import os

file_name="data_routier.json"
file_path_1 = f"ECO_TRANS/data/raw/{file_name}"
file_path_2 = f"ECO_TRANS/data/raw/LCD_sample_csv.csv"

##print(file_path)
##print(get_json_from_url("https://data.cityofnewyork.us/resource/i4gi-tjb9.json","ECO_TRANS/data/raw/data_routier.json"))
##print(get_json_from_url("https://openweathermap.org/api/air-pollution","ECO_TRANS/data/raw/Q_Air.json"))
print(get_data_csv(file_path_2))
##print(get_json_from_url("https://data.cityofnewyork.us/resource/i4gi-tjb9.json","data/raw/data_routier.json"))

# from data.raw.connection import load_json