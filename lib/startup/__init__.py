from flask import Flask, request

from lib.search import search
from lib.call import call



def init_app(url: str):
    """
    init_app Initialises the application
    
    Starts up the app, and sets the routes and listeners
    
    Args:
        url (str): url to send the search results to
    
    Returns:
        app (Flask_app object): Flask app object
    """
    
    app = Flask(__name__)
    
    @app.route("/google", methods=['POST'])
    def query():
        """
        Retreives query string from the brain and sends the query to the google search function, then sends it back to the brain
        """
        if request.method == "POST":
            #Retrieve query string
            query_string = request.form.get("Query")
            
            #Google Search
            search_results = search(query_string)
            
            #Sends them back out
            call(url, search_results)
            
    
    return app