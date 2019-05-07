'''
Created on Oct 24, 2018
DESCRIPTION: Use of 'Stop Finder' API to obtain details of stops within the New South Wales public transport network.
@author: Shirantha
'''

# Use the "requests" library to perform the request and to parse the JSON response
import requests

# Define different modes as per the Trip Planner API documentation
mode_def = {1: 'Train', 4: 'Light Rail',  5: 'Bus', 9: 'Wharf', 11: 'Ferry', 15: 'Taxi'}

# Define variable for "stop"
# Value for "stop" can take as an external input (future enhancement), so this test can be reused for multiple stops
stop = "Wynyard Station"

# Construct the URL using the "stop" value given
url="https://www.transportnsw.info/web/XML_STOPFINDER_REQUEST?TfNSWSF=true&language=en&name_sf=\"" + stop + "\"&outputFormat=rapidJSON&type_sf=any&version=10.2.2.48"

#Perform GET request using the URL
response = requests.get(url)

# Get the JSON content parsed and stored
data = response.json()

# Error handling
try:
    # The "response" is in JSON format containing dictionary and lists.
    # "modes" (a dictionary) can be accessed as below:
    modes = data['locations'][0]['modes']
except (KeyError, IndexError):
    # Throw exception in case the "stop" does not contain any modes (eg: "Qantas International Cooks River Av")
    # or if a non-existent "stop" is given. 
    print("No Modes of Transport found for " + stop)
    # Since there are no modes (our aim is to find modes), no point proceeding further, so exit.
    exit()
    
# We have found "modes", print them.
# As per the dictionary "mode_def", the code of each mode are mapped to their corresponing values (eg: 1=Train) 
print("Modes of Transport found for " + stop + ":")
for m in modes:
    print(mode_def[m])
