from django.shortcuts import render

def index(request):
    return render(request, 'homepage/home.html')

def contact(request):
    return render(request, 'temptext.html', {'message':  "<a href='mailto:will@ubctacs.org' class='link-dark'>will@ubctacs.org</a>"})

def developers(request):
    return render(request, 'temptext.html', {'message':  "<a href='https://github.com/svenbaertschi/mako' class='link-dark'>github (help here)</a>"})
