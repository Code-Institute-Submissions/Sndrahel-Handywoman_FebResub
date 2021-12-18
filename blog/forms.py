from django import forms
from .models import Comment, Post


class BlogForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('author', 'likes', 'like_count')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)
