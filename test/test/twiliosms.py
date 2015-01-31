from twilio.rest import TwilioRestClient


class TwilioSMS(TwilioRestClient):
    def __init__(self, sms_to, msg):
        self.account_sid = "AC710ce54ec742f46e8758bba762c6986f"
        self.auth_token  = "7937bdfa2978ba3419d20ad6628982b1"
        self.sms_from = "+353861800265"
        self.sms_to = sms_to
        self.client = TwilioRestClient(self.account_sid, self.auth_token)
        self.txt = msg

    def send_sms(self):
        try:
            message = self.client.messages.create(body=self.txt,
                to=self.sms_to, from_=self.sms_from)
        except:
            return False
        return True

if __name__ == '__main__':
    to = "+353872789354"    # Aidan
    # to = "+353857354527"    # Kevin
    # to = "+353872650540"    # Mark
    # to = "+353876818193"
    twilio_msg = TwilioSMS(to, "Hi from textMinder @ #hackmakethebank")
    result = twilio_msg.send_sms()
    print result