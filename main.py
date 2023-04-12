# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import config
import json

def findHomesIn60139():

    url = "https://us-real-estate.p.rapidapi.com/v2/for-sale-by-zipcode"

    querystring = {"zipcode": "60139", "offset": "0", "limit": "42"}

    headers = {
        "X-RapidAPI-Key": config.X-RapidAPI-Key,
        "X-RapidAPI-Host": config.X-RapidAPI-Host
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(response.text, f, ensure_ascii=False, indent=4)
    print(response.text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    findHomesIn60139()
#@TODO: run this and save data to a json file, perform ur stuff on that data file. COMMENT OUT FUNCT AFTER
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
