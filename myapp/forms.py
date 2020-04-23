from django import forms

from . import models


class SongFormWithModelChoiceField(forms.Form):
    """
    Form that accepts choices for the `artist` field as an argument.

    This will always run a query for choices when `is_valid()` runs.
    """
    title = forms.CharField(required=True, max_length=100)
    artist = forms.ModelChoiceField(queryset=models.Artist.objects.all())


class SongFormWithChoiceField(forms.Form):
    """
    Form that accepts choices for the `artist` field as an argument.

    This prevents some duplicate queries when used in loops.
    """
    title = forms.CharField(required=True, max_length=100)
    artist = forms.ChoiceField()

    def __init__(self, artist_choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['artist'].choices = artist_choices
