INVALID_MSG = 'Sorry you sent an invalid request.'


def get_balance(user, sms_body):
    balance = 13.00
    return 'HI %s, YOUR CURRENT BALANCE IS EUR %.2f.' % (user['name'], balance)



def set_pay(user, sms_body):
    body = sms_body.split(' ')
    limit = body[1]
    user['pay_limit'] = limit
    # write_user_settings()

    return 'PAYMENT NOTIFICATION LIMIT SET TO EUR %.2f. ' \
        'ONLY PAYMENTS GREATER THAN EUR %.2f WILL RESULT IN TEXT NOTIFICATION' % (float(limit), float(limit))


def set_receive(user, sms_body):
    body = sms_body.split(' ')
    limit = body[1]
    return 'INCOMING FUNDS NOTIFICATION LIMIT SET TO EUR %.2f. ' \
        'ONLY INCOMING FUNDS GREATER THAN EUR %.2f WILL RESULT IN TEXT NOTIFICATION' % (float(limit), float(limit))


def set_stop(user, sms_body):
    return 'CONFIRMATION YOU WILL NO LONGER RECEIVE TEXT NOTIFICATIONS.'


def set_start(user, sms_body):
    return 'TEXT NOTIFICATIONS WILL RESUME USING PREVIOUS SETTINGS.'

def get_sms_settings(user, sms_body):
    return 'Your settings are'

def write_user_settings():
    with io.open("users.json","w",encoding='utf-8') as fl:
        fl.write(unicode(json.dumps(_USERS, ensure_ascii=False)))

