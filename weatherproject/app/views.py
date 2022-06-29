from django.shortcuts import render
from django.http import HttpResponse 
import requests
# Create your views here.
def index(request):

    if 'city' in request.POST:
        city=request.POST['city']
    # else:
    #     city="Delhi"
        apiid="f36ec19d8d3a5ba2a62a995aabe69d44"
        url1="https://api.openweathermap.org/data/2.5/weather"
        param1={'q':city,'appid':apiid,'units':'metric'}
   
        r1=requests.get(url=url1,params=param1)
        r2=r1.json()
    
        disc=r2['weather'][0]['description']
        icon=r2['weather'][0]['icon']
        temp=r2['main']['temp']
        return render(request,"index.html",{'icon':icon,'temp':temp,'city':city,'disc':disc})
    # return HttpResponse("Haa ! bhai hua")
    # return render(request,"index.html",{'r2':r2})