import os
import requests
from pathlib import Path # to find path to the file
from dotenv import load_dotenv # to load/take the information with a file

def find_env():         
    base_dir = Path(__file__).resolve().parent.parent
    """
        __file__ = Finds /run/src/api.py
        parent = /run/src
        parent.parent = /run and finds .env
        parent.parent.etc...
    """
    # creates the path to .env file
    load_path = base_dir / ".env"

    return load_path

def fetch_data():
    # Loads the variables from .env into environment
    load_dotenv(find_env())

    # Location: Dallas, Texas, US
    CityName = "Dallas"

    # using .env, call the variable name, keeping API Key a Secret
    API_KEY = os.getenv("OPEN_API_KEY")

    URL = "https://api.openweathermap.org/data/2.5/weather" 

    CALL = f"{URL}?q={CityName}&appid={API_KEY}&units=imperial"

    try:
        response = requests.get(CALL, timeout=(3, 5)) # 3 sec MAX time to connect, 5 sec MAX time to wait for response
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh.args[0])
    except requests.exceptions.ReadTimeout as errrt:
        print("Time out")
    except requests.exceptions.ConnectionError as conerr:
        print("Connection error")
    except requests.exceptions.RequestException as errex:
        print("General Exception: Unknown error")

    if response.status_code == 200:
        data = response.json() # UPDATE: how does json file works

        temp = float(data["main"]["temp"])
        h_temp = int(data["main"]["temp_max"]) 
        l_temp =  int(data["main"]["temp_min"])
        
        return temp, h_temp, l_temp
    else:
        print("Error:", response.status_code)

if __name__ == "__main__":
    temp, h_temp, l_temp = fetch_data()
    print(temp, h_temp, l_temp)