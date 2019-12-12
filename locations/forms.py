from django import forms
from locations.models import Page

class PageForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:
        model = Page
        fields = ('title', 'content',)
