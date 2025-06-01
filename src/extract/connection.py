import pandas as pd
from json import loads
import json
import os 
import requests  


def get_json_from_url(url :str,filename:str) -> dict:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Ensure the directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Les données ont été sauvegardées dans '{filename}'.")
        return data 
    else:
        raise Exception(f"Failed to fetch data from {url}, status code: {response.status_code}")


def get_data_csv (file_path: str) -> pd.DataFrame:
    """
    Reads a CSV file and returns a pandas DataFrame.
    
    :param file_path: Path to the CSV file.
    :return: DataFrame containing the data from the CSV file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    File_csv =pd.read_csv(file_path,sep=',', encoding='utf-8')
    return File_csv
'''def load_json(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return loads(data)'''
