#!/usr/bin/env python3
##
## EPITECH PROJECT, 2026
## checker.py
## File description:
## checker.py
##

import requests
import os
from dotenv import load_dotenv

load_dotenv()

EPI_TOKEN = os.getenv("EPITECH_TOKEN")

def get_test_results():
    url = "https://my.epitech.eu/api/students/test-results?year=2025"

    headers = {
        "Authorization": f"Bearer {EPI_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    print(f"Status code : {response.status_code}")

    if response.status_code == 200 or response.status_code == 304:
        data = response.json()
        return data
    else:
        print(f"Error : {response.status_code}")
        return None

if __name__ == "__main__":
    results = get_test_results()
    if results:
        print(f"Number of projects : {len(results['results'])}")
        last = results['results'][40]
        print(f"Last project : {last['context']['title']}")
            
