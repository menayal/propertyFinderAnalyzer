from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
import sqlite3

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # return render(request, "index.html")
    context = {
        'api_key': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, "viewGUI/index.html", context)
def display_data(request):
    # Connect to the SQLite database
    conn = sqlite3.connect('../houses.db')
    cursor = conn.cursor()

    # Retrieve the data from the houses table
    cursor.execute("SELECT * FROM houses")
    data = cursor.fetchall()
    context = {
        'api_key': settings.GOOGLE_MAPS_API_KEY,
        'data': data
    }
    # Close the database connection
    cursor.close()
    conn.close()

    # Render the HTML template with the retrieved data
    return render(request, 'viewGUI/data_display.html', {'data': data},)
        #TODO: not sure why the context wont go in, api needs to be passed, get db displayed
