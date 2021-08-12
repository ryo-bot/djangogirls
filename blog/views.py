from django.shortcuts import render
from django.utils import timezone
#modelsの前の. = 同じディレクトリ　拡張子（.py）は必要ない
from .models import Post
#公開したBLOG記事を並べ替え



# Create your views here.

#post_listという関数を作成　引数はrequest
def post_list(request):
    #クエリセットを作成　変数はposts
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
