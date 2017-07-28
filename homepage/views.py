from django.shortcuts import render

def index(request):
    return render(request, 'homepage/home.html')

def contact(request):
    return render(request, 'temptext.html', {'message':  "<a href='mailto:will@ubctacs.org' style='text-decoration:none;'><h1>will@ubctacs.org</h1></a>"})
  
def developers(request):
    return render(request, 'temptext.html', {'message':  "<a href='https://github.com/svenbaertschi/mako' style='text-decoration:none;'><h1>github (help here)</h1></a>"})