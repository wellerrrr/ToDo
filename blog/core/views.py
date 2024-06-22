from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from config import TG_TOKEN


def index(request):
    return render(request, 'core/index.html', {'tg_admin': TG_TOKEN})


def admin(reqeust):
    return HttpResponse('You have been redirected!')