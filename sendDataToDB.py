import json
import sqlite3

# Load the data from the JSON file
with open("housing_data/houses10.json", "r") as file:
    data = json.load(file)

# Connect to the SQLite database
conn = sqlite3.connect('houses.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table to store the data
cursor.execute('''CREATE TABLE IF NOT EXISTS houses
                (address text, city text, state text, postal_code integer,
                 price real, bedrooms integer, sqft real, bathrooms integer)''')

# Insert the data into the database
for i in data["data"]["home_search"]["results"]:
    address = i['location']['address']['line']
    city = i['location']['address']['city']
    state = i['location']['address']['state_code']
    postal_code = i['location']['address']['postal_code']
    price = i['list_price']
    bedrooms = i['description']['beds']
    sqft = i['description']['sqft']
    bathrooms = i['description']['baths']
    cursor.execute("INSERT INTO houses VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (address, city, state, postal_code, price, bedrooms, sqft, bathrooms))

# Commit the changes to the database
conn.commit()

#
# for r in cursor.execute("select * from houses"):
#     print(r)
#
# print("************************************")
# cursor.execute("select * from houses where bathrooms=:b", {"b": 3})
# search = cursor.fetchall()
# print(search)
# Close the cursor and connection objects
cursor.close()
conn.close()