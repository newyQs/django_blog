from django.urls import path
from . import views

# 正在部署的应用的名称
app_name = 'comment'

urlpatterns = [
    path('post-comment/<int:article_id>/', views.post_comment, name='post_comment'),
]
