import io
import json

from pyramid.view import view_config

from openbank import account

INVALID_MSG = 'Sorry you sent an invalid request.'


def get_balance(user, sms_body):
    acc = account()
    balance = float(acc.getBalance(user['account_id'])['amount'])
    return 'Hi %s, your current balance is EUR %.2f.' % (user['name'], balance)


def set_pay(user, sms_body):
    body = sms_body.split(' ')
    limit = body[1]
    user['pay_limit'] = limit
    write_user_settings()
    return 'Hi %s, your payment notification limit set to EUR %.2f. Only payments greater ' \
        'than eur %.2f will result in text notification' % (user['name'],float(limit), float(limit))


def set_receive(user, sms_body):
    body = sms_body.split(' ')
    limit = body[1]
    user['receive_limit'] = limit
    write_user_settings()
    return 'Hi %s, your incoming funds notification limit set to EUR %.2f. Only incoming funds ' \
        'greater than eur %.2f will result in text notification' % (user['name'], float(limit), float(limit))


def set_stop(user, sms_body):
    user['sms_status'] = 'Off'
    write_user_settings()
    return 'Hi %s, confirmation that you will no longer receive automated text notifications.' % user['name']


def set_start(user, sms_body):
    user['sms_status'] = 'On'
    return 'Hi %s, automated text notifications will resume using previous settings.' % user['name']

def get_sms_settings(user, sms_body):
    return 'Hi %s, your TextMinder settings are: Pay limit = %d, ' \
           'Receive Limit = %d, Status = %s' % (user['name'], float(user['pay_limit']), \
                                                float(user['receive_limit']), user['sms_status'])

def write_user_settings():
    with io.open("users.json","w",encoding='utf-8') as fl:
        fl.write(unicode(json.dumps(_USERS, ensure_ascii=False)))


_COMMANDS = {'BALANCE': get_balance,
             'PAY': set_pay,
             'RECEIVE': set_receive,
             'STOP': set_stop,
             'START': set_start,
             'SETTINGS': get_sms_settings,
             }
"""
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
"""
with io.open("aidan.json","w",encoding='utf-8') as fl:
    fl.write(unicode(json.dumps({'aidan'}, ensure_ascii=False)))

with open("users.json") as json_file:
   _USERS = json.load(json_file)




@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'test'}


@view_config(route_name='messages', renderer='string')
def messages(request):
    sms_body = request.params.get('Body')
    sms_from = request.params.get('From')
    # user = sms_from
    print sms_from
    print sms_body
    user = _USERS.get(sms_from)
    if user is None:
        return 'You are not authorized for this service'

    try:
        return_msg = _COMMANDS[sms_body.upper().split(' ')[0]](user, sms_body)
    except:
        return_msg = INVALID_MSG

    return return_msg
