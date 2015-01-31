from pyramid.view import view_config
from twiliosms import TwilioSMS


def get_balance():
    return 'YOUR CURRENT BALANCE IS xxx'

def set_pay():
    return 'PAYMENT NOTIFICATION LIMIT SET TO XX. ONLY PAYMENTS GREATER THAN XX WILL RESULT IN TEXT NOTIFICATION'

_COMMANDS = {'BALANCE': get_balance,
             'PAY': set_pay,
             }


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'test'}

@view_config(route_name='messages', renderer='string')
def messages(request):
    sms_body = request.params.get('Body')
    sms_from = request.params.get('From')

    try:
        return_msg = _COMMANDS[sms_body]()
    except:
        return_msg = "Thank you for your text message."

    print return_msg

    return return_msg


