
import json
import pandas as pd
# Load the data from the JSON file

def findJson():
    # Load the data from the JSON file
    with open("housing_data/houses10.json", "r") as file:
        data = json.load(file)


    for i in data["data"]["home_search"]["results"]:
        print(f"{i['location']['address']['line']}, "
              f"{i['location']['address']['city']}, "
              f"{i['location']['address']['state_code']}, "
              f"{i['location']['address']['postal_code']}"
              f"\tPrice: {i['list_price']}")

    # print(pd.json_normalize(data["data"]["home_search"]["results"][0]))
    # print((data["data"]["home_search"]["results"][0]["location"]["address"]))
    #
    # print(f"{data['data']['home_search']['results'][0]['location']['address']['line']}, "
    #       f"{data['data']['home_search']['results'][0]['location']['address']['city']}, "
    #       f"{data['data']['home_search']['results'][0]['location']['address']['state_code']}, "
    #       f"{data['data']['home_search']['results'][0]['location']['address']['postal_code']}"
    #       f" Price: {data['data']['home_search']['results'][0]['list_price']}")


    # @todo use nlp to query the data


if __name__ == '__main__':
    findJson()