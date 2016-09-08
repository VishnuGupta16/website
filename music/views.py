from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Album,Song
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

def favourite(request,album_id):
    album = get_object_or_404(Album,pk=album_id)
    try:
        selected_song = album.song_set.get('song')
    except(KeyError , Song.DoesNotExist):
        return render(request,'music/detail.html',{
            'album':album,
            'error_message': 'Please select song from list'
                                                   })
    else:
        selected_song.is_favourite = True
        selected_song.save()
        return render(request,'music/detail.html',{'album':album})