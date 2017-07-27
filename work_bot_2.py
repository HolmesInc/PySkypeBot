from flask import Flask, request
from PySkype import SkypeBot
import os
import json

BOT_HOST = '127.0.0.1'
BOT_PORT = 8080
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CLIENT_ID = ''
CLIENT_PASSWORD = ''

app = Flask('WorkBot')
bot = SkypeBot(CLIENT_ID, CLIENT_PASSWORD, CURRENT_DIR)


@app.route('/api/messages', methods=['POST'])
def messages():
    if request.method == 'POST':
        data = json.loads(request.data.decode('utf8'))
        sender = data['conversation']['id']
        service = data['serviceUrl']
        bot.send_message(service, sender, "YEAH, I'm working!")
    else:
        print('not post request')
    return '<h1>Bot is working</h1>'


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host=BOT_HOST, port=BOT_PORT, debug=True)
