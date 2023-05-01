# propertyFinderAnalyzer
Welcome to Property Finder Analyzer, a web application designed to help you find and analyze real estate properties. 
This application allows you to search for properties based on location(limited to Glendale Heights for now) and other criteria, view their details, 
and analyze their potential profitability using various metrics such as cash on cash return.

Additionally, Property Finder Analyzer features a Cash on Cash Return Configuration tool, which allows you to input various expenses and financing options to calculate the potential cash on cash return for a given property. This tool provides you with valuable insights into the potential profitability of a property investment.
# Instructions:  
 * To run this web app locally:
	 * Clone this repo
	 * Install the dependencies and libraries:
		 * `pip install -r requirements.txt`
	 * Move into the `propFinderAnalyer` directory
		 * `cd propFinderAnalyer`
		 * To launch it, run:
			 * `python manage.py runserver`
			 * To see the development server that is started:
				 *  http://127.0.0.1:8000/
			 * This starts the web app and brings you to the index page. Currently, the **core functionality** is housed at display_data. Move to or click:
				 *  http://127.0.0.1:8000/viewGUI/display_data/
			 * You should now be able to see a list of properties in the Glendale Heights area.
			 * Properties are on the right and are also marked on the map.
               * If you do not see a map, reload the page. 
			 * To begin the cash on cash calculation, click the button on the top right called "cash on cash return configuration"
				 * Once inside the modal, enter the desired fields. Keeping in mind that you can skip a field and leave it empty.
				 * **Note:** if you are **purchasing a property with cash** with no mortgage, you have to type in "**cash**" in the down payment input. You do not need to type anything else in the loan information section.
               

# Dependencies:  
 * Need access to:
	 * US Real Estate API - only **300** calls a month for the free tier  
		 * https://rapidapi.com/datascraper/api/us-real-estate
	 * Google Maps JavaScript API - **200$** Free limit every month
		 * https://developers.google.com/maps/documentation/javascript/overview
 * Download punkt for tokenization  
 * Although not currently working, for the experimental NLP section, I used:
	 * Download the spacy english model   
	   * `python -m spacy download en_core_web_sm` (maybe covered in requirements.txt)  
	   * `python -m spacy download en_core_web_lg`   
	   * `python -m spacy download xx_ent_wiki_sm`  
	   * also installed:  
	     * Entity models downloads- could be deleted:  
	       * `nltk.downloader.download('maxent_ne_chunker')  
	           nltk.downloader.download('words')  
	           nltk.downloader.download('treebank')  
	           nltk.downloader.download('maxent_treebank_pos_tagger')  
	           nltk.downloader.download('punkt')  
	           nltk.download('averaged_perceptron_tagger')`
           
# Pesky problems and how I solved them:  

 *  Problem 1: After running `main.py` you receive a very large file with JSON content. Upon openning it, you'll see something along the lines of:
	  * `{\"status\":200,\"data\":{\"home_search\":{\"total\":46,\"count\":42,\"results\":[{\"primary_photo\":{\"href\":\"https:\\/\\/ap.rdcpix.com\\/4a17c00f7e2b5495801493679e4902a9l-m2568904874s-w1024_h768.jpg\"},\"last_update_date\":\"2023-04-28T18:40:54Z\",\"source\":{\"agents\":[{\"office_name\":\"Redfin Corporation\"},{\"office_name\":\"Redfin Corporation\"}],\"id\":\"CHIL\",\"plan_id\":null,\...`
* This is not usable for the application.
* Solution 1:
	* A quick and janky fix is to open the file and simply find and replace all the `\` in the file. You also need to replace the beginning and ending `"`
	* This should fix the problem and allow you to use the JSON file
    * If your using Pycharm, hitting Reformat Code will fix the indents too
  
* If you are trying to use a different json file from `main.py`, follow the steps in Problem 1 to fix. 
Then update the code in `sendDataToDB.py` and `propFinderAnalyer/viewGUI/views.py`
  * Run `sendDataToDB.py`
