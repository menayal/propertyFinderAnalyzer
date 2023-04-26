
import json
import pandas as pd
import nltk #tokenize
nltk.download('punkt')
import spacy #entity recognition
from spacy import displacy
nlp = spacy.load("en_core_web_lg") #load the eng model
# nlp = spacy.load(""xx_ent_wiki_sm"") #load the eng model

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
    #split it up

def querySplitAndAnalysis(query):
    tokens = nltk.word_tokenize(query)
    print(tokens)

    #for finding the locations in your query
    doc = nlp(query)

    for ent in doc.ents:
        # if ent.label_ == "GPE": # GPE for geopolitical entities like cities or countries.
        print(ent.text)

if __name__ == '__main__':
    # findJson()
    query = input("What kind of property are you looking for? Give me some details (city, price, sqft, rooms, bathrooms):\n"
                  "(Note: currently only works with one city(Glendale Heights)\n")
    querySplitAndAnalysis(query)

    # text = "When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously."


    doc = nlp(query)
    displacy.serve(doc, style="ent")
    
    #@todo work on NER for cities in IL only, including all suburbs, currently only works with big.expand it for prices,
        #@TODO schaumburg glen ellyn glendale heights willowbrook warrenville plainfield bloomingdale chicago
        # not working with these cities, keep researching the problem
    #@todo bathrooms, sqft etc...
    #@todo then use the locatation to map onto the web app map