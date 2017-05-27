from django.shortcuts import render
from django.http import HttpResponse
from services.web import login_check

# Create your views here.

@login_check
def index(req):
    return HttpResponse("Hello, I'm oneline. New style to achieve news.")


@login_check
def create_item(req):
    if req.method != 'POST':
        raise Exception('Not a post request!')

    return HttpResponse('You have post a oneline: ' + req.POST.get('title'))
