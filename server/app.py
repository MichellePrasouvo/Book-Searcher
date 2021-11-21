from flask import Flask
from flask import request
from urllib.request import urlopen
# from flask_cors import CORS 
import json 

app = Flask(__name__)

@app.route("/search")
def home():
    name = request.args.get('name')
    print(name)
    api = "https://www.googleapis.com/books/v1/volumes?q="
    # send a request and get a JSON response
    resp = urlopen(api + name.replace(" ", ""))
    book_data = json.load(resp)

    book_info = book_data["items"][0]["volumeInfo"]
    # print (volume_info)
    for key, val in book_info.items():
        print (key, val)

    print ("description:", book_info['description'])
    print("\n***\n")

    book_dict = {
        'author': book_info["authors"][0],
        'description': book_info['description'],
        'page_count': book_info['pageCount'],
        'published': book_info["publishedDate"],
        'rating': book_info['averageRating'],
        'category': book_info['categories'][0],
        'title':  name,
        'image': book_info['imageLinks']['thumbnail']
    }
    print (book_info)
    return book_dict 

