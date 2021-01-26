from django.http import HttpResponseRedirect
from django.urls import reverse

class AuthRequiredMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_request(self, request):
        print("OKIDOKILOKI")
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse("/blogg")) # or http response
        return None