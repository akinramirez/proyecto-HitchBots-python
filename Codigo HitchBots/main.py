#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
import requests

import httplib, urllib, base64
import json
# import os

from handler import receive_message

app = Flask(__name__)

#https://d8210649.ngrok.io/webhook

MY_SECRET = "Perspectiva"
TOKEN = "EAAMoNRv7regBABOfmDGgioBoZBu4m5DXjjn0PNKoZBYiYExmCSNPdnPhYMJqnbdVI0PqAVJtDc4LdCJQJMCwB3XeGQNrgoBWaYIpnzTH16U4TJmh7iWsRnbpZBmb0aAZBou4RFZCkSZAt9TKHMT8yQZCY1jXTDURTbwhTwKfkfU7IoHu0x3EUcv"


@app.route("/webhook", methods=["GET", "POST"])
def webhook():
	if request.method == "POST":
		payload = request.get_data()
		data =  json.loads(payload)

		for page_entry in data["entry"]:
			for message_event in page_entry["messaging"]:

				if "message" in message_event:
					receive_message(message_event, TOKEN)
		return "ok"

	else:
		verify_token = request.args.get("hub.verify_token", "")
		if verify_token == MY_SECRET:
			return request.args.get("hub.challenge", "")
		else:
			return "Token o secreto no valido."

# @app.route("/", methods = ['GET'])
# def index():
#   return 'Hola Bots!' 

@app.route('/')
def tagPhoto():
	# API request URL
    url = 'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/analyze'
    # url = 'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/describe?maxCandidates=1'


    # URL of the image you want tagged
    imageUrl = 'https://scontent-mia3-2.xx.fbcdn.net/v/t1.0-9/30530948_1880192975347192_5040619977417669929_n.jpg?_nc_cat=0&oh=f33be78b322616e62b126219231ca43f&oe=5B59B72B'



    # authorize the API call
    headers = dict()
    headers['Ocp-Apim-Subscription-Key'] = '717673c79ca74b47891b341bbbc4cf23'

    json = { 'url': imageUrl }
    params = { 'visualFeatures' : 'Tags' }
    data = None

     # get the response
    response = requests.request('post', url, json=json, data=data, headers=headers, params=params)

    # get status code
    status = response.status_code

    # get tags
    tags = ''
    response_tags = response.json()['tags']    
    for tag in response_tags:
        tags = tags + str(tag['name']) + ' '

    # print tags
    return tags
    


if __name__ == "__main__":
	app.run(port = 9000, debug = True)