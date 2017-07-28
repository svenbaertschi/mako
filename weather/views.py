from django.shortcuts import render
from weather.forms import PostForm
import requests
import json

# Create your views here.
def weather(request):


	if request.method=='POST':
		content = request.POST['location']
		form = PostForm(initial={'location':content})
		data = requests.get("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22"+content+"%22)%20and%20u%3D'c'&format=json").json()
		if data['query']['results']:
			effectiveroot = data['query']['results']['channel']
			locale = effectiveroot['location']
			condition = effectiveroot['item']['condition']
			forecast = effectiveroot['item']['forecast'][0]
			return render(request, 'weather/index.html', {'condition':condition, 'forecast':forecast, 'form':form, 'locale':locale} )
		else:
			return render(request, 'weather/unknownlocale.html', {'form':form} )
	else:
		content = 'Vancouver, CA'
		form = PostForm(initial={'location':'Vancouver, BC'})
		data = requests.get("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22"+content+"%22)%20and%20u%3D'c'&format=json").json()
		effectiveroot = data['query']['results']['channel']
		locale = effectiveroot['location']
		condition = effectiveroot['item']['condition']
		forecast = effectiveroot['item']['forecast'][0]
		return render(request, 'weather/index.html', {'condition':condition, 'forecast':forecast, 'locale':locale, 'form':form} )




	