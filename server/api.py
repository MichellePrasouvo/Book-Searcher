import json 
from urllib.request import urlopen

while True:
    api = "https://www.googleapis.com/books/v1/volumes?q="
    book = input ("Enter book name:")

    # send a request and get a JSON response
    resp = urlopen(api + book)
    book_data = json.load(resp)

    volume_info = book_data["items"][0]["volumeInfo"]
    # print (volume_info)
    author = volume_info["authors"]
    # practice with conditional expressions!
    prettify_author = author if len(author) > 1 else author[0]

    print ("description:", volume_info['description'])

    print("\n***\n")

    # ask user if they would like to enter another isbn
    user_update = input("Would you like to enter another book? y or n ").lower().strip()

    if user_update != "y":
        print("May the Zen of Python be with you. Have a nice day!")
        break # as the name suggests, the break statement breaks out of the while loop