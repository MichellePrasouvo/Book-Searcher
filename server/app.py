from flask import Flask
from flask import request
from urllib.request import urlopen
from flask_cors import CORS 
import json 

app = Flask(__name__)
CORS(app)


@app.route("/search")
def home():
    name = request.args.get('name')
 
    api = "https://www.googleapis.com/books/v1/volumes?q="
    # send a request and get a JSON response
    resp = urlopen(api + name.replace(" ", ""))
    book_data = json.load(resp)

    book_infos = []
    for i in book_data["items"]:
        book_info = i["volumeInfo"]

        book_dict = {}
        key_list = ['authors', 'pageCount', "publishedDate", 'averageRating', 'title', 'description', "imageLinks"]
        for key in key_list:
            if key in book_info:
                book_dict[key] = book_info[key]
            else:
                book_dict[key] = ''

        if 'authors' in book_dict:
            book_dict['authors'] = book_dict['authors'][0]
        if 'imageLinks' in book_dict:
            book_dict['imageLinks'] = book_dict['imageLinks']['thumbnail']
        book_infos.append(book_dict)
    result = {'results': book_infos}
    return result
            


