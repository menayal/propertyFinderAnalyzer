import json

config = {
    "X_RapidAPI_Key":"10e9a1cd5fmsh506c200fa507e36p176d58jsnd6a8596d70fe",
    "X_RapidAPI_Host":"us-real-estate.p.rapidapi.com",
    "GoogleMapAPIKey":"AIzaSyBtfXknSTNc6D59LHagI1iR1IKC2coeWXk"
}

with open('config.json', 'w') as f:
    json.dump(config, f)