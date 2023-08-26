import lib.googlesearch

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
    google_results = lib.googlesearch.search(query_string, num_results=3, advanced=True)

    #Parse results dictionary
    results["Query"] = query_string
    if google_results != []:
        results["Status"] = 200
    else:
        results["Status"] = 503
        
    results["Results"] = [{"Title" : result.title, "Description" : result.description} for result in google_results]

    
    return results

#print(search("Where are good places to eat in Singapore"))