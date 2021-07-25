#ブログポストを定義する場所
#from,importで他のファイルから必要な部分を取得する
from django.conf import settings
from django.db import models
from django.utils import timezone

#classでオブジェクトを定義していることを示す
#def...関数（ファンクション）
#classキーワードに続く行はインデントする
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
