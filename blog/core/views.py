from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'core/index.html')


def admin(reqeust):
    return HttpResponse('You have been redirected!')