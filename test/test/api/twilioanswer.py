from webob import Response, exc
from cornice import Service


from . import (
    API_ROOT,
    CORS_POLICY,
)

messages = Service(name='messages', '/messages', description="Messages")

class _apiError(exc.HTTPError):

    def __init__(self, errcode=401, msg='Unauthorized'):
        body = {'status': errcode, 'message': msg}
        Response.__init__(self, json.dumps(body))
        self.status = errcode
        self.content_type = 'application/json'


@messages.get()
@messages.post()
def get_messages(request):
    print request

