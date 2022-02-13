from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator  # 引入django的分页模块
from django.db.models import Q

from .models import ArticlePost  # 引入model层的数据表类
from .forms import ArticlePostForm  # 引入表单类
from comment.models import Comment

import markdown


# Create your views here.

# test
# def article_list(request):
#     return HttpResponse("Hello World!")


# 文章列表
def article_list(request):
    search = request.GET.get('search')
    order = request.GET.get('order')
    # 用户搜索逻辑
    if search:
        if order == 'total_views':
            # 用 Q对象 进行联合搜索
            article_list = ArticlePost.objects.filter(
                Q(title__icontains=search) |
                Q(body__icontains=search)
            ).order_by('-total_views')
        else:
            article_list = ArticlePost.objects.filter(
                Q(title__icontains=search) |
                Q(body__icontains=search)
            )
    else:
        # 将 search 参数重置为空
        search = ''
        if order == 'total_views':
            article_list = ArticlePost.objects.all().order_by('-total_views')
        else:
            article_list = ArticlePost.objects.all()

    paginator = Paginator(article_list, 3)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    # 增加 search 到 context
    context = {
        'articles': articles,
        'order': order,
        'search': search
    }
    return render(request, 'article/list.html', context)


# 文章详情
def article_details(request, id):
    article = ArticlePost.objects.get(id=id)  # 取出id=id的文章
    comments = Comment.objects.filter(article=id)
    # 浏览量 +1
    article.total_views += 1
    article.save(update_fields=['total_views'])
    article.body = markdown.markdown(
        article.body,
        extensions=[
            # 包含 缩写、表格等常用扩展
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',
            # 目录扩展
            'markdown.extensions.toc',
        ]
    )
    context = {
        "article": article,
        'comments': comments
    }
    return render(request, "article/detail.html", context)


# 创建文章
def article_create(request):
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=request.user.id)
            new_article.save()
            return redirect("article:article_list")
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    else:
        article_post_form = ArticlePostForm()
        context = {
            'article_post_form': article_post_form
        }
        return render(request, "article/create.html", context)


# 修改文章
def article_update(request, id):
    article = ArticlePost.objects.get(id=id)
    # 过滤非作者的用户
    if request.user != article.author:
        return HttpResponse("抱歉，你无权修改这篇文章。")

    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.title = request.POST.get("title")
            article.body = request.POST.get("body")
            article.save()
            return redirect("article:article_detail", id=id)
        else:
            return HttpResponse('表单内容有误，请重新填写。')
    else:
        article_post_form = ArticlePostForm()
        context = {
            "article": article,
            "article_post_form": article_post_form
        }
        return render(request, "article/update.html", context)


# 删除文章
def article_delete(request, id):
    article = ArticlePost.objects.get(id=id)
    article.delete()
    return redirect("article:article_list")


# 安全删除文章
def article_safe_delete(request, id):
    if request.method == "POST":
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅允许post请求。")
