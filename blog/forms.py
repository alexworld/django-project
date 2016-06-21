from django import forms
from .models import Person, Post, Comment
from django.contrib.auth.forms import AuthenticationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('username', 'password', 'first_name', 'last_name')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'text')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
