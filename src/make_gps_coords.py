# Author: Michael Novotny
# this script is to take the schools.csv file and create a new file with the
# gps coordinates for each school, indexed by school id
# Google maps will give you a 200 dollar credit for free, which is more than enough.

import csv
import json
import requests
import time
import os
from dotenv import load_dotenv
from urllib import parse

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
dotenv_path = os.path.join(project_root, '.env')
load_dotenv(dotenv_path)

MAPS_KEY = os.getenv("MAPS_API_KEY")
SCHOOLS = '../data/school.csv'

# read in the schools.csv file
schools = []
with open(SCHOOLS, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        schools.append(row)

# create a new file with the gps coordinates
with open('../data/schools_gps.csv', 'w') as f:
    fieldnames = ['School ID', 'lat', 'lng']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    progress_counter = 0
    for school in schools:
        progress_counter += 1
        # get the gps coordinates using google maps api
        address = ''
        if school['School Name'] != '':
            address += school['School Name'] + ', '
        if school['City'] != '':
            address += school['City'] + ', '
        if school['State'] != '':
            address += school['State']
        # make address url safe
        address = parse.quote(address)
        url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={MAPS_KEY}'
        response = requests.get(url)
        data = json.loads(response.text)
        # if the API call fails, try again
        while not data:
            time.sleep(1)
            response = requests.get(url)
            data = json.loads(response.text)
        # write the data to the new file
        try:
            location = data['results'][0]['geometry']['location']
        except IndexError:
            print(f'Error: {school["School ID"]}')
            print(data)
            location = {'lat': 0, 'lng': 0}

        writer.writerow({'School ID': school['School ID'],
                        'lat': location['lat'], 'lng': location['lng']})
        # print progress
        print(f'{school["School ID"]},{location["lat"]},{location["lng"]}')
        print(f'Progress: {progress_counter}/{len(schools)}')
