
import os
import json
import time
import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth

try:
    from tkinter import *
except ImportError as e:
    import tkinter 


course_info = {}
current_course_info = {}


filename = os.getcwd()+'\course_details.json'

#check to see if file containing json data exits in the direstory
if os.path.exists(filename):
    text_file = os.path.basename(filename)
    with open(text_file, 'r') as lines:
        #read through the file as a python object
            json_text = json.load(lines) 
            course_info['id'] = json_text['id']
            course_info['price'] = json_text['price_detail']['amount']
            old_price = course_info['price']


#Auhtentication details
client_id  = '' #your client id
client_secret = '' #your client secret
#get response from udemy
response = requests.get('https://www.udemy.com/api-2.0/courses/{course goes here}', auth=HTTPBasicAuth(client_id, client_secret)).json()

response_str = json.dumps(response, indent=2)


#open new data recieved from udemy
with open('course_details.json', 'w') as json_datas:
        json_datas.write(response_str)

text_file = os.path.basename(filename)
with open(text_file, 'r') as lines:
    #read through the file as a python object
            json_text = json.load(lines) 
            current_course_info['price'] = json_text['price_detail']['amount']
            new_price = current_course_info['price']

#check for price changes
if old_price - new_price == 0:
    old_price_state = "Prices havent changed yet"

    root = Tk()
    status = Label(root, text="Prices havent changed yet")
    exit()
    root.mainloop()

# Delay excution for one day! you dont want to keep sending requsts to udemy every second
    time.sleep(86400)
    time.sleep(5)
    print("done sleeping")

if old_price - new_price > 0: 
    f"Prices have changed from {old_price} to {new_price}"
    
if old_price - new_price < 0:
    f"Cost Just went up"
