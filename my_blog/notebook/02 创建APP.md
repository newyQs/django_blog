
## 创建一个app
```
python manage.py startapp article
```

其结构如下：
```
my_blog
│  db.sqlite3
│  manage.py
│
├─article
│  │  admin.py
│  │  apps.py
│  │  models.py
│  │  tests.py
│  │  views.py
│  │  __init__.py
│  │
│  └─migrations
│        └─ __init__.py
│
└─my_blog
    │  settings.py
    │  urls.py
    │  wsgi.py
    └─ __init__.py
```
### 项目结构分解
+ 根目录my_blog下有两个文件：db.sqlite3是一个轻量级的数据库文件，用来存储项目产生的数据，
  比如博客文章；manage.py是项目执行命令的入口，比如runserver。
  
+ 目录article是刚创建出来的app，用来存放博客文章相关的代码：后台管理文件admin.py，数据模型文件models.py，
  视图文件views.py，存放数据迁移文件的目录migrations。
  
+ 根目录下还有一个my_blog目录，其中的settings.py包含项目的配置参数，urls.py则是项目的根路由文件。

## 注册app (settings)
在my_blog目录的settings.py，找到INSTALLED_APPS写入如下代码：
```
my_blog/settings.py

INSTALLED_APPS = [
    # 其他代码
    ...

    # 新增'article'代码，激活app
    'article',
]
```

## 配置访问路由（urls）
```python
# my_blog/urls.py

from django.contrib import admin
# 记得引入include
from django.urls import path, include

# 存放映射关系的列表
urlpatterns = [
    path('admin/', admin.site.urls),
    # 新增代码，配置app的url
    path('article/', include('article.urls', namespace='article')),
]
```
django路由的用法：
+ article/分配了app的访问路径，在开发环境下，article的url为：http://127.0.0.1:8000/article/；
+ include是将路径分发到下一步处理。这里分发到article目录下的urls处理（注意创建这个urls）；
+ namespace保证反查到唯一的url，即使不同的app使用了相同的url；

## 配置分发路由的urls

```
article/urls.py

# 引入path
from django.urls import path

# 正在部署的应用的名称
app_name = 'article' # Django2.0之后，app的urls.py必须配置app_name，否则会报错

urlpatterns = [
    # 目前还没有urls
]
```

## 