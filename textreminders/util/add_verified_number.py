from twilio.rest import Client, TwilioException
from textreminders.util.settings import account_sid, auth_token


def add_verified_number(number):
    client = Client(account_sid, auth_token)
    try:
        validation_request = client.validation_requests.create(number,call_delay='15', friendly_name=number)
    except TwilioException:
        return 'ALREADY VERIFIED'

    return validation_request.validation_code
