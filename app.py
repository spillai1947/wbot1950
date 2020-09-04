from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openpyxl

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    """resp = MessagingResponse()"""
    """resp.message("You said: {}".format(msg))"""
    if msg == "Hello":
        resp = MessagingResponse()
        resp.message("Hey!!! there. Hope you are doing good")
    if msg == "What is your name?":
        resp = MessagingResponse()
        resp.message("My name is Rigel")   
    if msg == "Who created you?":
        resp = MessagingResponse()
        resp.message("Sumeet is the creator")
    if msg == "Status":
        resp = MessagingResponse()
        loc = ("https://github.com/spillai1947/wbot1950/blob/master/Auto.xlsx")
        wb = openpyxl.load_workbook(loc)
        sheet = wb['WAPP']
        msg1 = sheet.cell(1,1).value
        resp.message(msg1)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
