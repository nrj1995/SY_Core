from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import *

 

class BlogPostForm(forms.ModelForm):

    content = forms.CharField(widget=CKEditorWidget())

 

    class Meta:

        model = BlogPost

        fields = ['Nation','state','photo_1','title', 'content']

 
class CommentForm(forms.ModelForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = Comment
        fields = ['name','email','text']