from django.shortcuts import render
from django.http import HttpResponse


def index(request):
        return render(request, 'homepage/home.html')

def contact(request):
        return render(request, 'homepage/contact.html')