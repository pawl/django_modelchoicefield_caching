from django.db import connection
from django.http import HttpResponse

from . import forms, models


def index(request):
    playlist = [
        {
            "title": "Toosie Slide",
            "artist": 1
        },
        {
            "title": "The Man",
            "artist": 2
        },
        {
            "title": "Godzilla",
            "artist": 3
        },
        {
            "title": "Shape Of You",
            "artist": 4
        },
        {
            "title": "dangerous woman",
            "artist": 5
        },
        {
            "title": "7 rings",
            "artist": 5  # same artist as previous song
        }
    ]

    for song in playlist:
        form_data = {'title': song["title"], 'artist': song["artist"]}
        song_form = forms.SongFormWithModelChoiceField(data=form_data)
        song_form.is_valid()  # runs a query to get the ModelChoiceField queryset each time

    print('ModelChoiceField - query count AFTER validating all songs:',
          len(connection.queries))  # 6 queries

    # query for choices outside of the loop to prevent unnecessary queries
    artist_choices = [(artist.pk, artist.name)
                      for artist in models.Artist.objects.all()]
    for song in playlist:
        form_data = {'title': song["title"], 'artist': song["artist"]}
        # pass choices into the Form
        song_form = forms.SongFormWithChoiceField(
            artist_choices=artist_choices,
            data=form_data)
        song_form.is_valid()

    print('ChoiceField w/ choices passed in - query count AFTER validating all songs:',
          len(connection.queries))  # 7 queries (only 1 more query!)

    # TODO: find a good way to do the caching inside of the form?
    # maybe caching all choices would be bad due to memory issues (should at least be optional)
    # but caching duplicate requests for the same artist should be possible
    # solution should not make more than one network request
    # cache must expire after the request (assume the data can change, can't use local memory cache)
    # assume this runs on multiple servers (can't just bust the cache locally)
    # maybe this would work?: https://github.com/anexia-it/django-request-cache
    # unfortunately django-request-cache doesn't work with falsy values
    # and it does some hacks to make the request object available globally

    return HttpResponse(status=200)
