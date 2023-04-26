import requests
import config
import json
from decouple import config
#Gets the data from the API and stores it in a file. Currently not for real time use...



def findHomesIn60139():

    url = "https://us-real-estate.p.rapidapi.com/v2/for-sale-by-zipcode"

    querystring = {"zipcode": "60139", "offset": "0", "limit": "10"}

    headers = {
        "X-RapidAPI-Key": config('X_RapidAPI_Key'),
        "X-RapidAPI-Host": config('X_RapidAPI_Host')
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # with open('data.json', 'w', encoding='utf-8') as f:
    #     json.dump(response.text, f, ensure_ascii=False, indent=4)
    print(response.text)

# if __name__ == '__main__':
#     findHomesIn60139()


