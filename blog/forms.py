from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    # image = forms.ImageField(upload_to='static/')
    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            "category",
            "image",
        )
        widgets = {
            "content":forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.TextInput(attrs={"class": "form-control"}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            "content", "created_by",
       )
        widgets = {
            "content": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.TextInput(attrs={"class": "form-control"}),
        }