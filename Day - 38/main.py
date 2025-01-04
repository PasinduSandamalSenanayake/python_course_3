import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GENDER = "Male"
WEIGHT_KG = "78"
HEIGHT_CM = "165"
AGE = "25"

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": float(WEIGHT_KG),  # Ensure this is numeric
    "height_cm": float(HEIGHT_CM),  # Ensure this is numeric
    "age": int(AGE)  # Ensure this is numeric
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
