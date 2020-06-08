# Imports
'''3rd Party'''

'''Django official'''
from django import forms
from django.conf import settings
'''Project related'''
from .models import Essay
from jsys.globals import GlobalVariables


# Global variables
MAX_ESSAY_TITLE_LENGTH = GlobalVariables.MAX_ESSAY_TITLE_LENGTH
MAX_ESSAY_CONTENT_LENGTH = GlobalVariables.MAX_ESSAY_CONTENT_LENGTH


# Forms
''' Create New Essay Form '''
class EssayCreateForm(forms.ModelForm):
    title = forms.CharField(label='TITLE', widget=forms.TextInput(attrs={'class':' '}))
    content = forms.CharField(label='ESSAY CONTENT', widget=forms.Textarea(attrs={"rows":5, "cols":20, 'class':' '}))

    class Meta:
        model = Essay
        fields = ['title', 'content']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) > MAX_ESSAY_TITLE_LENGTH:
            raise forms.ValidationError(f'Your title can not be longer than {MAX_ESSAY_TITLE_LENGTH} characters.')
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > MAX_ESSAY_CONTENT_LENGTH:
            raise forms.ValidationError(f'Your essay content can not be longer than {MAX_ESSAY_CONTENT_LENGTH} characters.')
        return content
