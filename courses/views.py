from django.shortcuts import render

def index(request):
    return render(request, 'temptext.html', {'message':'<h1>todo: b-s pricing model</h1>'})
