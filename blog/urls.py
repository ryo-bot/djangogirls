from django.urls import path
#djangoのpath関数とblogアプリの全てのビューをインポートする
from . import views

#post_listという名前のビューをルートURLに割り当てる
urlpatterns = [
    path ('', views.post_list, name='post_list'),
    #投稿の内容を表示するpost_detailというビューをDjangoに示す
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit')
]