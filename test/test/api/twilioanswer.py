from webob import Response, exc
from cornice import Service
import json

messages = Service(name='messages', '/messages', description="Messages")

class _apiError(exc.HTTPError):

    def __init__(self, errcode=401, msg='Unauthorized'):
        body = {'status': errcode, 'message': msg}
        Response.__init__(self, json.dumps(body))
        self.status = errcode
        self.content_type = 'application/json'


@messages.get()
def get_messages(request):
    return {'incoming': json.dumps(request)}

@messages.get()
def post_messages(request):
    print request

