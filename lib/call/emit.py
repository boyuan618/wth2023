import requests


def call(url: str, results: dict) -> None:
    """
    call Sends the results to the given url
    
    Takes the results and sends them to the given url with requests

    Args:
        url (str): Url to send the results to
        results (dict): Results, aka the data, to be sent
    """
    requests.post(url, json=results)