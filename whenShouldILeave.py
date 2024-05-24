
import os
from dotenv import load_dotenv
import requests
import subprocess
import pushover

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


# This sends a notification to the Mac OS using osascript
# if travel_time:
#     message = f"Travel time from {origin} to {destination} by car: {travel_time}"

#     # Send notification on Mac
#     subprocess.run(['osascript', '-e', f'display notification "{message}" with title "Travel Time"'])
#     print("Notification sent!")
# else:
#     print("API key not found in environment variables.")
def send_pushover_notification(user_key, api_token, message):
    url = 'https://api.pushover.net/1/messages.json'
    data = {
        'token': api_token,
        'user': user_key,
        'message': message,
        'title': 'Travel Time Notification'
    }
    response = requests.post(url, data=data)
    return response.status_code == 200

api_key = os.getenv('API_KEY')
origin = 'Seattle, WA'
destination = 'Los Angeles, CA'

travel_time = get_travel_time(api_key, origin, destination)

if travel_time:
    message = f"Travel time from {origin} to {destination} by car: {travel_time}"
    user_key = os.getenv('PUSHOVER_USER_KEY')
    api_token = os.getenv('PUSHOVER_API_KEY')
    
    if send_pushover_notification(user_key, api_token, message):
        print("Notification sent!")
    else:
        print("Failed to send notification.")
else:
    print("API key not found in environment variables.")