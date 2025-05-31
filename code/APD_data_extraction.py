# Data scraping: NASA's API
# Author: Antonio Merchant
# Date: May 31, 2025

# Import libraries
import os
from dotenv import load_dotenv
import pandas as pd
import requests
from datetime import datetime, timedelta

# API KEY
load_dotenv()
API_KEY = os.getenv('NASA_KEY')

# Date function
def fetch_apod_range(start_date, end_date):
    url = "https://api.nasa.gov/planetary/apod" # NASA's API
    params = {
        "api_key": API_KEY,
        "start_date": start_date,
        "end_date": end_date
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return []

    return response.json()


# Function to get batches
def get_days_of_apod():
    total_days = 1000 # Total days of pictures
    batch_size = 100 # Number of batches to efficiency
    all_data = []

    end_date = datetime.today()
    start_date = end_date - timedelta(days=total_days - 1)

    current_start = start_date

    for i in range(0, total_days, batch_size):
        current_end = min(current_start + timedelta(days=batch_size - 1), end_date)
        print(f"Lote: {current_start.strftime('%Y-%m-%d')} → {current_end.strftime('%Y-%m-%d')}")

        batch = fetch_apod_range(
            current_start.strftime("%Y-%m-%d"),
            current_end.strftime("%Y-%m-%d")
        )

        for item in batch:
            all_data.append({
                "date": item.get("date"),
                "title": item.get("title"),
                "explanation": item.get("explanation"),
                "url": item.get("url")
            })

        current_start = current_end + timedelta(days=1)

    return all_data

# Save the dataframe
data = get_days_of_apod()
df = pd.DataFrame(data)
PATH = os.path.join('data', 'astronomic_album.csv')
df.to_csv(path_or_buf=PATH, index=False)
