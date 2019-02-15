from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    template = loader.get_template('dca/index.html')
    return render(request, 'dca/index.html')
