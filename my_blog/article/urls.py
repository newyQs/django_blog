from django.urls import path
from . import views

# 正在部署的应用的名称
app_name = 'article'

urlpatterns = [
    # app添加的url配置
    path("article_list/", views.article_list, name="article_list"),
    path("article_detail/<int:id>/", views.article_details, name="article_detail"),
    path("article_create/", views.article_create, name="article_create"),
    path("article_update/<int:id>/", views.article_update, name="article_update"),
    path("article_delete/<int:id>/", views.article_delete, name="article_delete"),
    path("article_safe_delete/<int:id>/", views.article_safe_delete, name="article_safe_delete"),

]
