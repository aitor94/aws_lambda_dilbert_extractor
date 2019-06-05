import json
from telegram.ext import  Updater
import requests
import lxml.html


def dilbert(event, context):
    updater = Updater(token='Your Telegram bot token')
    dispatcher = updater.dispatcher

    response = requests.get("http://dilbert.com/")
    doc = lxml.html.document_fromstring(response.text)
    element = doc.xpath('//*[@id="js_comics"]/div/div[1]/div/section/div[2]/a/img')[0]
    keys = element.keys()
    values = element.values()
    dictionary = dict(zip(keys, values))
    image_url = str(dictionary["src"])

    chat_id = 12345678 # Put here the chat id of your telegram bot
    updater.bot.send_photo(chat_id = chat_id, photo = "http:" + image_url)

    body = {
        "message": "Lambda launched successfully!!!!!!!!!!!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
