import urllib.request, json
# Configure API request
endpoint = "https://developer.nps.gov/api/v1/parks?stateCode=me"
HEADERS = {"Authorization":"INSERT_API_KEY_HERE"}
req = urllib.request.Request(endpoint,headers=HEADERS)
# Additional code would follow
