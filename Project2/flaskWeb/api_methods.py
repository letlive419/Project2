from flaskWeb import main_functions
import requests



def request_key():
    apiDict = main_functions.read_from_file("flaskWeb/JSON_Documents/api_key.json")
    return apiDict['key']

def request_title(title_name):
    url1 = "https://api.nytimes.com/svc/books/v3/reviews.json?title=" + title_name + "&api-key=" + request_key()
    response = requests.get(url1).json()
    return response

def request_date(date,list_name):
    url2 = "https://api.nytimes.com/svc/books/v3/lists/" + date + "/" + list_name + ".json&api-key=" + request_key()
    response2 = requests.get(url2).json()
    return response2
def request_author(author_name):
    url3 = "https://api.nytimes.com/svc/books/v3/reviews.json?author=" + author_name + "&api-key=" + request_key()
    response3 = requests.get(url3).json()
    return response3