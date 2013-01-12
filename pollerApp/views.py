# Create your views here.

from django.http import HttpResponse
import datetime

def home(request):
    now  = datetime.date.now()
    html = "<html><body> Welcome to ePolling system <br/> Today is '%s'.</body></html>"%now
    return HttpResponse(html)

def login(request):
    return HttpResponse("login here")

def logout(request):
    return HttpResponse("Logout redirects here")

def register(request):
    return HttpResponse("Register here")