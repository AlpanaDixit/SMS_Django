from twilio.base.exceptions import TwilioRestException
from django.shortcuts import render
from .sms_utils import send_sms

def send_sms_view(request):
    to_phone_number = '+917666894190'
    message = 'My Lovely Alpana'
    
    try:
        message_sid = send_sms(to_phone_number, message)
        return render(request, 'sms_sent.html', {'message_sid': message_sid})
    except TwilioRestException as e:
        error_message = f"Error sending SMS: {e.msg}"
        return render(request, 'sms_error.html', {'error_message': error_message})
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return render(request, 'sms_error.html', {'error_message': error_message})
