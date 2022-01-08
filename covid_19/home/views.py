from django.shortcuts import render
from django.views.generic import View , TemplateView


def home(request):
    return render(request, 'home.html')
