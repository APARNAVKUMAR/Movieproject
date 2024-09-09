from django import forms

from myapp.models import MovieDb


class MovieForm(forms.ModelForm):
    class Meta:
        model    =   MovieDb
        fields  =   '__all__'