from django import forms
from .models import Cblogs


class BlogForm(forms.ModelForm):
    class Meta:  # Meta class is used to specify additional options for a form
        model = Cblogs
        fields = ['title', 'body', 'text',
                  'author', 'developer', 'header_image']

        # now to do the styling add widgets to the form
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'developer': forms.TextInput(attrs={'class': 'form-control'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),

        }
