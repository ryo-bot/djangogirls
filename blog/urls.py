from django.urls import path
#djangoのpath関数とblogアプリの全てのビューをインポートする
from django.urls.resolvers import URLPattern
from . import views

#post_listという名前のビューをルートURLに割り当てる
URLPatterns = [
    path ('', views.post_list, name='post_list'),
]