import requests
import os
from datetime import datetime

GENDER = "MALE"
WEIGHT_KG = "60"
HEIGHT = "160.5"
AGE = "50"

APP_ID = "842ebc98"
API_KEY = "7c99a521010f3e024917bc8b269fdf4b"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_input = input("Tell which exercise you did today?: ")
sheet_endpoint = "https://api.sheety.co/f9c4fac30ef9a7b17cfff75b41329599/workoutTracking38/workouts"

header = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,

}

parameters = {
 "query": exercise_input,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT,
 "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    # print(sheet_response.text)

    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            "My_kate_B",
            "kotek123123",
        )
    )