# from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.conf import settings
from re import compile

EXEMPT_URLS = [ compile(url) for url in getattr(settings, "LOGIN_EXEMPT_URLS",() ) ]
a = EXEMPT_URLS.append(compile(getattr(settings, "LOGIN_URL","accounts/login/").lstrip('/'))) # [re.compile('accounts/login/')]
print ('a', a)
class GlobalLoginMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.login = self.process_request(request)
        response = self.get_response(request) # to get the response from later middleware and the view
        return response

    def process_request(self,request):
        print ('request', request)
        if request.user.is_authenticated():
            return None

        path = request.path_info.lstrip('/') # removes or clears the precedented /

        if any(url.match(path) for url in EXEMPT_URLS):
            print('matched')
            return None
        print (getattr(settings, "LOGIN_URL", "accounts/login/"))
        return redirect('/accounts/login')
