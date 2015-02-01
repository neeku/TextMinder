from pyramid.view import view_config

from commands import *

_COMMANDS = {'BALANCE': get_balance,
             'PAY': set_pay,
             'RECEIVE': set_receive,
             'STOP': set_stop,
             'START': set_start,
             'SETTINGS': get_sms_settings,
             }

_USERS = {'+353872789354': {'account_id': '',
                            'name': 'Aidan',
                            'pay_limit': 20.00,
                            'receive_limit': 20.00,
                            'sms_status': 'On'},
          '+353857354527': {'account_id': '',
                            'name': 'Kevin',
                            'pay_limit': 20.00,
                            'receive_limit': 20.00,
                            'sms_status': 'On'},
          '+353834446388': {'account_id': '',
                            'name': 'Neeku',
                            'pay_limit': 20.00,
                            'receive_limit': 20.00,
                            'sms_status': 'On'},
          '+353871111111': {'account_id': '',
                            'name': 'Robin',
                            'pay_limit': 20.00,
                            'receive_limit': 20.00,
                            'sms_status': 'On'},
}


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'test'}


@view_config(route_name='messages', renderer='string')
def messages(request):
    sms_body = request.params.get('Body')
    sms_from = request.params.get('From')
    user = sms_from
    """
    print sms_from
    user = _USERS.get(sms_from)
    if user is None:
        return 'You are not authorized for this service'
    """
    try:
        return_msg = _COMMANDS[sms_body.split(' ')[0]](user, sms_body)
    except:
        return_msg = INVALID_MSG

    return return_msg
