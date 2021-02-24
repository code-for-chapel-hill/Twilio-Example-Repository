import os

from flask import Flask, url_for, render_template, request
from twilio.rest import Client

app = Flask(__name__)

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client()

@app.route('/')
def index():
    return render_template(
        'index.html', 
        css=url_for('static', filename='style.css'),
        js=url_for('static', filename='sendsms.js')
    )

@app.route('/api/sendMessage', methods=['POST'])
def send_message():
    from_number = os.environ["TWILIO_FROM_NUMBER"]
    data = request.get_json()
    to_number = data['number']
    message = data['message']

    message = client.messages.create(body = message, from_ = from_number, to = to_number)

    return {'success': True}, 200


if __name__ == '__main__':
    app.run(debug=True, port=3000)