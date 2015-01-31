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

@view_config(route_name='messages', renderer='json')
def messages(request):
    sms_body = request.params.get('Body')
    sms_from = request.params.get('From')

    return_msg = _COMMANDS[sms_body]()

    print return_msg
    if return_msg:
        sms_msg = TwilioSMS(sms_from, return_msg)
        result = sms_msg.send_sms()

    return {'status': 'OK'}


