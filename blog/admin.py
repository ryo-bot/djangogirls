#前回定義したpostモデルをインポート
from django.contrib import admin
from .models import Post
#同じ階層なら　'.~' で呼び出せる。　from .apps import BlogConfig
#モデルをadminページで見られるようにするため、登録する
admin.site.register(Post)