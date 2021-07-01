import os
import requests
from datetime import datetime


APP_ID = os.getenv("appid")
API_KEY = os.getenv("apikey")

nutritionix_endpoint = os.getenv("ntrnix_endpoint")
sheety_endpoint = os.getenv("shty_endpoint")

user_query = input("What did you do today? ")

parameters = {
    "query": user_query,
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}


response = requests.post(url=nutritionix_endpoint, json=parameters, headers=headers)

data = response.json()
exercises_data_list = data["exercises"]

exercises_list = [{"exercise": exercise["name"], "duration": exercise["duration_min"],
                   "calories": exercise["nf_calories"]} for exercise in exercises_data_list]

today = datetime.now()
date_formatted = today.strftime("%d/%m/%Y")

time = today.time()
time_formatted = time.strftime("%H:%M:%S")

for exercise in exercises_list:
    my_workout = {
        "workout": {
            "date": date_formatted,
            "time": time_formatted,
            "exercise": exercise["exercise"].title(),
            "duration": exercise["duration"],
            "calories": exercise["calories"],
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, json=my_workout)


