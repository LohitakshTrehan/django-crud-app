from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from app1.models import *
# Create your views here.

def artists(request):
    a=Artist.objects.all()
    #return HttpResponse('<html><head><title>Hello, Django!</title></head><body><h1>Hello, Django</h1></body></html>')
    return render_to_response('artists.html',{'artists':a})
def artistdetails(request,id):
    artist = Artist.objects.get(pk = id)
    return render(request,'artistdetails.html',{'artist':artist})
def artistcreate(request):
    if request.method == 'GET':
        form = ArtistForm()
        return render(request,'create.html',{'form':form})
    elif request.method=='POST':
        form = ArtistForm(request.POST)
        form.save()
        return HttpResponseRedirect('/artists')
