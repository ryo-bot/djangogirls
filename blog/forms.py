# 最初にdjangoのforms、Postモデルをimportする
from django import forms

from .models import Post

# PostForm=フォームの名前
class PostForm(forms.ModelForm):

    class Meta:
        # フォームのフィールドに置くものを指定
        model = Post
        fields = ('title', 'text',)