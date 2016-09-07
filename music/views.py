from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Album
from django.http import Http404
from django.template import loader
# Create your views here.


def index(request):


    #connect to database

    all_album = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
         'all_album':all_album
    }
    return HttpResponse(template.render(context,request))


def detail(request,album_id):
    ''' try:
         album = Album.objects.get(pk=album_id)
     except Album.DoesNotExist:
         raise Http404("Album does not exit")'''  # shortcut is below
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})

