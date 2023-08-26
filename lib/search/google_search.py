import googlesearch

def search(query_string: str) -> dict:
    """
    search A function to search google
    
    Takes in a query string, searches google and takes the first 3 results

    Args:
        query_string (str): A query string to be searched in google

    Returns:
        results (dict): Returns a dictionary in the format:
                        {
                            "Query": Query_String, 
                            "Status": Status,
                            "Results": [
                                {
                                    "Title_1", Description_1
                                }, 
                                {
                                    "Title_2", Description_2
                                },
                                {
                                    "Title_3", Description_3
                                }
                            ]
                        } 
    """
    results = {}
    
    #Query google
    google_results = googlesearch.search(query_string, num_results=3, advanced=True)
    
    #Parse results dictionary
    results["Query"] = query_string
    results["Status"] = 200
    results["Results"] = []
    
    #Adding search results
    for google_result in google_results:
        result = {}
        result[google_result.title] = google_result.description
        
        results["Results"].append(result)
    
    return results
