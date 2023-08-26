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
            "Title", Title_1
            "Description", Description_1
        }, 
        {
            "Title", Title_2
            "Description", Description_2
        },
        {
            "Title", Title_3
            "Description", Description_3
        }
    ]
}

Status Codes: 
    200: Ok
    500: No internet
    503: No result found