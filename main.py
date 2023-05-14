import requests
from datetime import datetime

APP_ID = "YOUR APP ID"
API_KEY = "YOUR API KEY"

food_endpoint = "https://trackapi.nutritionix.com/v2"

exercise_endpoint = f"{food_endpoint}/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

exercise_params = {
    "query": input("Tell me which exercise you did?"),
    "gender": "male",
    "weight_kg": "60",
    "height_cm": "180",
    "age": "20"
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()
print(result)

#Saving data to spreadsheet

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheety_endpoint = "https://api.sheety.co/efd0e36cf97c69e390156b77ecaba0d5/workoutTracking/workouts"

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

    sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=headers)

    print(sheet_response.text)
