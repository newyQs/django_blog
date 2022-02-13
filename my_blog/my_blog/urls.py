"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # 新增代码，配置的URL位置：
    # 参数article/分配了app的访问路径，include将路径分发给下一步处理，namespace保证反查到唯一的url，即使不同的app使用了相同的url

    # 文章信息app
    path("article/", include('article.urls', namespace='article')),
    # 用户管理app
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
    # 重置密码app：第三方集成
    path('password-reset/', include('password_reset.urls')),
    # 评论管理app
    path('comment/', include('comment.urls', namespace='comment')),
]

# 配置上传的图片的URL路径
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
