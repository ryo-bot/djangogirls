from django.urls import path
#djangoのpath関数とblogアプリの全てのビューをインポートする
from . import views

#post_listという名前のビューをルートURLに割り当てる
urlpatterns = [
    path ('', views.post_list, name='post_list'),
    #投稿の内容を表示するpost_detailというビューをDjangoに示す
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]