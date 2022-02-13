取出数据并展示数据

## Hello World!
```python
# article/views.py

# 导入 HttpResponse 模块
from django.http import HttpResponse

# 视图函数
def article_list(request):
    return HttpResponse("Hello World!")
```

### 解析
网页都是从视图派生而来。每一个视图表现为一个简单的Python函数，它必须要做的只有两件事：
返回一个包含被请求页面内容的 HttpResponse对象，或者抛出一个异常，比如 Http404 。

视图函数中的request与网页发来的请求有关，里面包含get或post的内容、用户浏览器、系统等信息。
Django调用article_list函数时会返回一个含字符串的 HttpResponse对象。

### 配置urls
```python
# article/urls.py

# 引入views.py
from . import views

...

urlpatterns = [
    # path函数将url映射到视图
    path('article_list/', views.article_list, name='article_list'),
]
```
Django 将会根据用户请求的 URL 来选择使用哪个视图。
本例中当用户请求article/article_list/链接时，会调用views.py中的article_list函数，并返回渲染后的对象。
参数name用于反查url地址，相当于给url起了个名字，以后会用到。

### 调试
打开浏览器输入：
```
http://127.0.0.1:8000/article/article_list/
```

## 将模型表注册到后台
```python
# article/admin.py

from django.contrib import admin
# 导入ArticlerPost
from .models import ArticlePost

# 注册ArticlePost到admin中
admin.site.register(ArticlePost)
```

### 查看后台
```
http://127.0.0.1:8000/admin/
```