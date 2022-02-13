
## 改写如下：
```python
# article/views.py

from django.shortcuts import render
# 导入数据模型ArticlePost
from .models import ArticlePost

def article_list(request):
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    # 需要传递给模板（templates）的对象
    context = { 'articles': articles }
    # render函数：载入模板，并返回context对象
    return render(request, 'article/list.html', context)
```
### 代码解析
+ from .models import ArticlePost从models.py中导入ArticlePost数据类
+ ArticlePost.objects.all()是数据类的方法，可以获得所有的对象（即博客文章），并传递给articles变量
+ context定义了需要传递给模板的上下文，这里即articles
+ 最后返回了render函数。它的作用是结合模板和上下文，并返回渲染后的HttpResponse对象。
  通俗的讲就是把context的内容，加载进模板，并通过浏览器呈现。

render的变量分解如下：
+ request是固定的request对象，照着写就可以
+ article/list.html定义了模板文件的位置、名称
+ context定义了需要传入模板文件的上下文

## 编写模板（template）
在根目录下新建templates文件夹，再新建article文件夹，再新建list.html文件，即：
```
my_blog
│  ...
├─article
│  ...
└─my_blog
│  ...
└─templates
    └─ article
        └─ list.html
```
在list.html文件中写入：
```html
<!--templates/article/list.html-->

{% for article in articles %}
    <p>{{ article.title }}</p>
{% endfor %}
```
在settings.py中，加入代码os.path.join(BASE_DIR, 'templates')：
```
my_blog/settings.py

TEMPLATES = [
    {
        ...
        # 定义模板位置
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]
```
