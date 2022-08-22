from django.http import HttpResponse
from urllib import request
from django.shortcuts import render
import requests


def github(request):
    url = 'http://api.github.com/orgs/stackbuilders/repos'
    response = requests.get(url)
    return render(request,'github.html',{'response':response.text})
