
import os
from notion.client import NotionClient
from flask import Flask
from flask import request


app = Flask(__name__)


def createTweet(token, collectionURL, tweet, author, url):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL)
    row = cv.collection.add_row()
    row.tweet = tweet
    row.author = author
    row.address = url


def createTask(token, collectionURL, content):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL)
    row = cv.collection.add_row()
    row.name = content


def createReceipt(token, collectionURL, product, content, url, date):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL)
    row = cv.collection.add_row()
    row.product = product
    row.content = content
    row.url = url
    row.date = date


def createEmail(token, collectionURL, sender, subject, message_url):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL)
    row = cv.collection.add_row()
    row.sender = sender
    row.subject = subject
    row.message_url = message_url


@app.route('/twitter', methods=['GET'])
def twitter():
    tweet = request.args.get('tweet')
    author = request.args.get('author')
    tweetURL = request.args.get('url')
    token_v2 = os.environ.get("TOKEN")
    url = os.environ.get("URL")
    createTweet(token_v2, url, tweet, author, tweetURL)
    return f'added {tweet} to Notion'


@app.route('/todoist', methods=['GET'])
def todoist():
    todo = request.args.get('todo')
    token_v2 = os.environ.get("TOKEN")
    url = os.environ.get("URL")
    createTask(token_v2, url, todo)
    return f'added {todo} to Notion'


@app.route('/gmailreceipts', methods=['GET'])
def gmailReceipt():
    product = request.args.get('product')
    content = request.args.get('content')
    message_url = request.args.get('url')
    date = request.args.get('date')
    token_v2 = os.environ.get("TOKEN")
    url = os.environ.get("URL")
    createReceipt(token_v2, url, product, content, message_url, date)
    return f'added {product} receipt to Notion'


@app.route('/createemail', methods=['GET'])
def gmailUrgentEmail():
    sender = request.args.get('sender')
    subject = request.args.get('subject')
    message_url = request.args.get('url')
    token_v2 = os.environ.get("TOKEN")
    url = os.environ.get("URL")
    createEmail(token_v2, url, sender, subject, message_url)
    return f'added email from {sender} to Notion'


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
