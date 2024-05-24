# WhenShouldILeave
Python Automation with Google Maps Distance Matrix API that calculates the drive time between my house and work (It finds the drive time between any two locations)

## How To Use 
1. Create a Google Cloud Platform (GCP) Account: If you don't already have one, sign up for a Google Cloud Platform account at https://cloud.google.com/.

2. Enable the Distance Matrix API: Once you have access to the Google Cloud Console, navigate to the API Library and enable the Distance Matrix API. You can find it by searching for "Distance Matrix API" in the API Library.

3. Create an API Key: After enabling the API, you need to create an API key. Go to the Credentials section in the Google Cloud Console, create a new API key, and restrict it to only allow requests from your specific application or website (optional but best practice for security to restrict it)

4. Create an account on Pushover.net and verify your email, take note of your user key

5. Click on the API tab and register your app to get an API key

6. Clone the repository and open in your preferred Code IDE (I use VSCode for this one)

7.  Run `pip install python-dotenv requests pushover subprocess` to install the required dotenv, requests, pushover, and subprocess packages (subprocess is only needed for Mac Notifications)

8.  Create a `.env` file to store your api key, add the following variablea `API_KEY='Your_GoogleAPI_Key'` `PUSHOVER_USER_KEY="Your_User_Key` and `PUSHOVER_API_KEY="Your_PushoverAPI_Key` into the .env file

9. Download the pushover app, login to the same account as online, and turn on notifications

10.  Run the script with `python3 whenShouldILeave.py` - you should recieve push notifications from the app

 11. EXTRA: If you want to recieve the message on your Mac or in terminal simply uncomment the part that mentions it

### NOTE:
To change your origin and end destination, simply open the whenShouldILeave.py in a code editor and replace origin and destination
(Can be City, State, Address, etc.)

### PS:
I will make an interactive version soon where you don't have to change the values in the Python file but this is more convienient for my use case since I'm always mapping to the same place.
