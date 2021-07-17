import os

from flask import Flask, Response

from twilio.twiml.voice_response import VoiceResponse
# from twilio.rest import Client

from decouple import config

# from pyngrok import ngrok

app = Flask(__name__)

# Pull in configuration from system environment variables
TWILIO_ACCOUNT_SID = config('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = config('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = config('TWILIO_PHONE_NUMBER')

# create an authenticated client that can make requests to Twilio for your
# account.
# client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# http_tunnel = ngrok.connect()

# ssh_tunnel = ngrok.connect(22, "tcp")

@app.route('/')
def hello_word():
    return 'Hello World'

@app.route('/hello', methods=['GET', 'POST'])
def hello_twi_ml():
    response = VoiceResponse()
    response.say('Hello there! You have successfully configured a web hook.')
    response.say('Good luck on your Twilio quest!', voice='woman')
    return Response(str(response), mimetype='text/xml')



if __name__ == '__main__':
    app.run(debug=True)