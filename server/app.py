from flask import Flask
from flask import request
from urllib.request import urlopen
# from flask_cors import CORS 
import json 

app = Flask(__name__)

@app.route("/search")
def home():
    name = request.args.get('name')
    
    api = "https://www.googleapis.com/books/v1/volumes?q="
    # send a request and get a JSON response
    resp = urlopen(api + name.replace(" ", ""))
    book_data = json.load(resp)

    volume_info = book_data["items"][0]["volumeInfo"]
    print (volume_info)


    print ("description:", volume_info['description'])
    print("\n***\n")
    return volume_info['description']

