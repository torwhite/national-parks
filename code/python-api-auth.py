import urllib.request, json, os

# Retrieve API key from local system
NP_API = os.environ.get('NP_API')

# Configure API request
endpoint = "https://developer.nps.gov/api/v1/parks?stateCode=me"
HEADERS = {"Authorization":"NP_API"}
req = urllib.request.Request(endpoint,headers=HEADERS)

# Additional code would follow
