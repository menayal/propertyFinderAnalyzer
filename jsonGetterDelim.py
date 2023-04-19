import json
import pandas as pd
import nltk  # tokenize
# nltk.download('punkt')
import spacy  # entity recognition



def findJson():
    # Load the data from the JSON file
    with open("housing_data/houses10.json", "r") as file:
        data = json.load(file)

    # for i in data["data"]["home_search"]["results"]:
    #     print(f"{i['location']['address']['line']}, "
    #           f"{i['location']['address']['city']}, "
    #           f"{i['location']['address']['state_code']}, "
    #           f"{i['location']['address']['postal_code']}"
    #           f"\tPrice: {i['list_price']}\n"
    #           f"Rooms: {i['description']['beds']}, "
    #           f"Sqft: {i['description']['sqft']}, "
    #           f"Baths: {i['description']['baths']}")
    data_list = []

    for i in data["data"]["home_search"]["results"]:
        data_dict = {
            "address": i['location']['address']['line'],
            "city": i['location']['address']['city'],
            "state": i['location']['address']['state_code'],
            "postal_code": i['location']['address']['postal_code'],
            "price": i['list_price'],
            "bedrooms": i['description']['beds'],
            "sqft": i['description']['sqft'],
            "bathrooms": i['description']['baths']
        }
        data_list.append(data_dict)
    pd.set_option('display.max_columns', None)
    df = pd.DataFrame(data_list)

    print(df)
def querySplitAndAnalysis(query):
    queryTokenList = query.split(",")
    return queryTokenList




if __name__ == '__main__':
    findJson()
    query = input(
        "What kind of property are you looking for? Give me some details (city, max price, sqft, rooms, bathrooms):\n"
        "(Note: currently only works with one city(Glendale Heights)\n"
        "Enter each field separated by a comma. Enter nothing if you have no preference.\n"
        "Example request: Glendale heights, 150000,,2,1:\n")
    queryTokenList = querySplitAndAnalysis(query)
    print(queryTokenList)


