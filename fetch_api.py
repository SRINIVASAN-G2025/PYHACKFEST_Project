import os
from datetime import datetime

import requests
from pymongo import MongoClient

API_KEY = os.getenv("OPENWEATHER_API_KEY", "YOUR_API_KEY").strip()

if API_KEY == "YOUR_API_KEY":
    raise SystemExit(
        "ERROR: Please set a valid OpenWeather API key in the OPENWEATHER_API_KEY environment variable."
    )

LAT = 13.0827
LON = 80.2707
URL = (
    "http://api.openweathermap.org/data/2.5/air_pollution"
    f"?lat={LAT}&lon={LON}&appid={API_KEY}"
)


def main():
    response = requests.get(URL, timeout=10)
    data = response.json()

    if response.status_code != 200 or "list" not in data:
        raise SystemExit(f"API ERROR: {data}")

    components = data["list"][0]["components"]
    aqi = data["list"][0]["main"]["aqi"]

    record = {
        "region": "Chennai",
        "aqi": aqi,
        "pm25": components.get("pm2_5"),
        "pm10": components.get("pm10"),
        "co2": components.get("co"),
        "date": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
    }

    client = MongoClient("mongodb://localhost:27017/")
    db = client["pollution_db"]
    collection = db["pollution"]

    collection.insert_one(record)
    print("✅ API data inserted into MongoDB")
    print(record)


if __name__ == "__main__":
    main()