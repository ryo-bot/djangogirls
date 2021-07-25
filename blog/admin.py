#前回定義したpostモデルをインポート
from django.contrib import admin
from .models import Post

#モデルをadminページで見られるようにするため、登録する
admin.site.register(Post)