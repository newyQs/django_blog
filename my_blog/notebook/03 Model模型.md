
Django 框架主要关注的是模型（Model）、模板（Template）和视图（Views），称为MTV模式。

主要职责如下：
+ 模型（Model）         即数据存取层，处理与数据相关的所有事务： 如何存取、如何验证有效性、包含哪些行为以及数据之间的关系等。
+ 模板（Template）      即业务逻辑层，处理与表现相关的决定： 如何在页面或其他类型文档中进行显示。
+ 视图（View）          即表现层，存取模型及调取恰当模板的相关逻辑。模型与模板的桥梁。

简单来说就是Model存取数据，View决定需要调取哪些数据，而Template则负责将调取出的数据以合理的方式展现出来。

## 数据库与模型
对象关系映射（Object Relational Mapping，简称ORM）

## 编写models.py
```python
# article/models.py

from django.db import models
from django.contrib.auth.models import User # 导入内建的User模型。
from django.utils import timezone # timezone 用于处理时间相关事务。

# 博客文章数据模型
class ArticlePost(models.Model):
    # 文章作者。参数 on_delete 用于指定数据删除的方式
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 文章标题。models.CharField 为字符串字段，用于保存较短的字符串，比如标题
    title = models.CharField(max_length=100)
    # 文章正文。保存大量文本使用 TextField
    body = models.TextField()
    # 文章创建时间。参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)
    # 文章更新时间。参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)
```
注：
+ 每个模型都要继承与models.Model，这里有操作数据库的所有方法。
+ 每个字段都是Field类的实例。比如字符串是CharField，日期是DateTimeField。表示存储字段的数据类型。
+ 定义某些字段Field类的实例可能需要一些参数。比如CharField需要一个max_length参数，这个参数的用处不仅是用于定义数据库结构，也是用于验证数据。
+ 使用ForeignKey定义一个关系，这告诉django，每个（或多个）ArticlePost对象都关联到User对象。

文章数据类型，定义了一篇文章所必要的参数：作者，标题，正文，创建时间，更新时间。其他参数可以拓展。

另外还可以额外定义一些内容，规范数据行为：
```python
# article/models.py

...

class ArticlePost(models.Model):
    ...

    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)

    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        # return self.title 将文章标题返回
        return self.title
```
如 Meta类中的ordering定义了模型返回数据的排列顺序是按照创建时间created的倒序展示的，即表示"-created"。
而__str__参数定义调用str对象返回的内容。

整理如下：
```python
# article/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
```

## 代码解读

### 类
类（Class）和实例（Instance）:
类是抽象的模板，而实例是根据这个类创建出来的一个个具体的“对象”。
每个对象都拥有相同的方法，但各自的数据可能不同。而这些方法被打包封装在一起，就组成了类。

比如说我们刚刚写的这个ArticlePost类，作用就是就为博客文章的内容提供了一个模板。每当有一篇新文章生成的时候，
都要比对ArticlePost类来创建author、title、body...等等数据；虽然每篇文章的具体内容可能不一样，但是必须都遵循相同的规则。

在Django中，数据由模型来处理，而模型的载体就是类（Class）。

### 字段
字段（field）表示数据库表的一个抽象类，Django使用字段类创建数据库表，并将Python类型映射到数据库。
在模型中，字段被实例化为类属性并表示特定的表，同时具有将字段值映射到数据库的属性及方法。
比方说ArticlePost类中有一个title的属性，这个属性中保存着Charfield类型的数据：即一个较短的字符串。

### 外键
数据库中有各种各样的数据表，有时候几张表的数据是互相关联的。
比如一张表记录了所有的文章，另一张表记录了所有的用户，而文章是用户发表的，这时候这两张表就产生了关系。
外键就是用来表示这种关系的。

而ForeignKey是用来解决“一对多”关系的。那什么又叫“一对多”？
在我们的ArticlePost模型中，一篇文章只能有一个作者，而一个作者可以有很多篇文章，这就是“一对多”关系。
又比如一个班级的同学中，每个同学只能有一种性别，而每种性别可以对应很多的同学，这也是“一对多”。
因此，通过ForeignKey外键，将User和ArticlePost关联到了一起，最终就是将博客文章的作者和网站的用户关联在一起了。

既然有“一对多”，当然也有“一对一”（OneToOneField）、“多对多”（ManyToManyField）。

### 内部类
内部类class Meta提供模型的元数据。元数据是“任何不是字段的东西”，
例如排序选项ordering、数据库表名db_table、单数和复数名称verbose_name和 verbose_name_plural。
这些信息不是某篇文章私有的数据，而是整张表的共同行为。

要不要写内部类是完全可选的，当然有了它可以帮助理解并规范类的行为。

在ArticlePost中我们使用的元数据ordering = ('-created',)，表明了每当我需要取出文章列表，
作为博客首页时，按照-created（即文章创建时间，负号标识倒序）来排列，保证了最新文章永远在最顶部位置。

## 数据迁移（Migrations）
```
python manage.py makemigrations
python manage.py migrate
```