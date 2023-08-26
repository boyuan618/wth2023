# wth2023

A info bank where a query from the brain is made to google and then the first few results with its description are returned to the brain.


tts <- brain <- stt
         |
         V
      info bank (query to google)


Takes in a query string in json format of:
{
    "Query": Query_String
}

Returns the results from google in json format of:
{
    "Query": Query_String, 
    "Status": Status,
    "Results": [
        {
            "Title_1", Description_1
        }, 
        {
            "Title_2", Description_2
        }
    ]
}