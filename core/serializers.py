from django.forms import fields
from rest_framework import serializers
from .models import Post

from django import forms

# class PostForm(forms.modelForm):
#     class Meta:
#         model = Post
#         fields = {
#             "title",'description'
#         }


class PostSerilizer(serializers, serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = {
            'title': "description"
        }
