
import os
from dotenv import load_dotenv
import requests

load_dotenv()
def get_travel_time(api_key, origin, destination, mode='driving'):
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&mode={mode}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200 and data['status'] == 'OK':
        travel_time = data['rows'][0]['elements'][0]['duration']['text']
        return travel_time
    else:
        return None

api_key = os.getenv('API_KEY')
origin = '4745 16th Ave NE, Seattle, WA 98105'
destination = '7671 Seaview Ave NW, Seattle, WA 98117'

travel_time = get_travel_time(api_key, origin, destination)
print(f"Travel time from {origin} to {destination} by car: {travel_time}")
