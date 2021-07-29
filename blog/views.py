from django.shortcuts import render

# Create your views here.

#post_listという関数を作成　引数はrequest
def post_list(request):
    return render(request, 'blog/post_list.html', {})

