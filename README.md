### Twilio Example

This project is meant to serve as an example of how to integrate text messaging via the Twilio platform into your website.

# Steps

1. Create an account on twilio.com.

2. On your dashboard, look for your account sid and auth token

3. Put those in your environment as TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN respectively.

4. Go to https://www.twilio.com/console/phone-numbers

5. Buy a number using the "Buy a number" button in the top right.

6. Put the digits of this number in your environment as TWILIO_FROM_NUMBER

7. Run python app.py from the project base directory.

The example should now be serving on localhost:3000