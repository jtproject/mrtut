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
a,b = 'ex. "Breaking Fake News"','ex. "Do you really need an example???"'

# Forms
''' Create New Essay Form '''
class EssayCreateForm(forms.ModelForm):
    title = forms.CharField(label='title', required=False, widget=forms.TextInput(attrs={'placeholder':a}))
    content = forms.CharField(label='essay content', required=False, widget=forms.Textarea(attrs={'placeholder':b}))

    class Meta:
        model = Essay
        fields = ['title', 'content']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) > MAX_ESSAY_TITLE_LENGTH:
            raise forms.ValidationError(f'Your title can not be longer than {MAX_ESSAY_TITLE_LENGTH} characters.')
        if not title:
            raise forms.ValidationError(f'This field is required.')
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > MAX_ESSAY_CONTENT_LENGTH:
            raise forms.ValidationError(f'Your essay content can not be longer than {MAX_ESSAY_CONTENT_LENGTH} characters.')
        if not content:
            raise forms.ValidationError(f'This field is required.')
        return content
