"""
model里面的每一个类都是数据库中的一张表。
1. django字段的数据类型；
2.

每当model里的数据发生变化:
1. 创建新的迁移表
python manage.py makemigrations
2. 应用迁移至数据库
python manage.py migrate
"""
from django.db import models
from django.contrib.auth.models import User  # 引入自带的User
from django.utils import timezone  # 用于处理时间
from django.urls import reverse


# Create your models here.

class ArticlePost(models.Model):  # 每个模型都应该是django.db.models.Model 类的子类，继承了操作数据库需要的所有方法
    """
    文章模型表
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 文章作者，on_delete 用于指定数据删除的方式
    title = models.CharField(max_length=100)  # 文章标题，CharField字符字段
    body = models.TextField()  # 文章详情，保存大文本使用TextField字段
    created = models.DateTimeField(default=timezone.now)  # 创建时间
    updated = models.DateTimeField(default=timezone.now)  # 更新时间
    total_views = models.PositiveIntegerField(default=0)  # 文章浏览量

    # 内部类
    class Meta:
        """
        定义数据的行为
        即表示，最新创建的放在最上面展示
        比如有：
            ordering
            db_table
            verbose_name
            verbose_name_plural
        """
        ordering = ("-created",)  # 定义排序，created表示创建顺序，-created表示以创建时间的倒序

    def __str__(self):
        """
        返回文章的标题
        """
        return self.title

    def get_absolute_url(self):
        """
        获取文章地址
        """
        return reverse('article:article_detail', args=[self.id])
