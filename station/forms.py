# Imports
'''3rd Party'''

'''Django official'''
from django import forms
from django.conf import settings
'''Project related'''
from .models import Station
from jsys.globals import GlobalVariables


# Global variables
MAX_STATION_NAME_LENGTH = GlobalVariables.MAX_STATION_NAME_LENGTH
MAX_STATION_CATEGORY_LENGTH = GlobalVariables.MAX_STATION_CATEGORY_LENGTH
MAX_STATION_BIO_LENGTH = GlobalVariables.MAX_STATION_BIO_LENGTH


# Forms
''' Create New Essay Form '''
class StationCreateForm(forms.ModelForm):
    name = forms.CharField(label='name', required=False, widget=forms.TextInput(attrs={}))
    category = forms.CharField(label='category', required=False, widget=forms.TextInput(attrs={}))
    bio = forms.CharField(label='station bio', required=False, widget=forms.Textarea(attrs={}))

    class Meta:
        model = Station
        fields = ['name', 'category', 'bio']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) > MAX_STATION_NAME_LENGTH:
            raise forms.ValidationError(f'Your station name can not be longer than {MAX_STATION_NAME_LENGTH} characters.')
        if not name:
            raise forms.ValidationError('This field is required.')
        return name

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if len(category) > MAX_STATION_CATEGORY_LENGTH:
            raise forms.ValidationError(f'Your station category can not be longer than {MAX_STATION_CATEGORY_LENGTH} characters.')
        if not category:
            raise forms.ValidationError('This field is required.')
        return category

    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if len(bio) > MAX_STATION_BIO_LENGTH:
            raise forms.ValidationError(f'Your station bio can not be longer than {MAX_STATION_BIO_LENGTH} characters.')
        if not bio:
            raise forms.ValidationError('This field is required.')
        return bio
