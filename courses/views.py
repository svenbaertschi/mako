from django.shortcuts import render
from django.http import HttpResponse


def index(request):
        return render(request, 'temptext.html', {'message':'<h1>nothing here yet</h1>'})
