from django.db import reset_queries
from django.http import request
from django.shortcuts import render
from django.utils import timezone
#modelsの前の. = 同じディレクトリ　拡張子（.py）は必要ない
from .models import Post
# Page Not Found 404 ページ
from django.shortcuts import render, get_object_or_404
# 投稿ページ
from .forms import PostForm
# 新しく作成された投稿ページを表示
from django.shortcuts import redirect

# Create your views here.

#post_listという関数を作成　引数はrequest
def post_list(request):
    #クエリセットを作成　変数はposts
    #公開したBLOG記事を並べ替え
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
#リクエストされたpk（プライマリキー）のページを表示する 
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# 新しい投稿ページを表示する
def post_new(request):
# 空白のフォームか、フォームデータが入力された状態かで分岐する
# 『POST』は送られてきたものを意味する変数
    if request.method == "POST":
        form = PostForm(request.POST)
        # 必須フィールドがきちんと入力されているかチェック
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})
    