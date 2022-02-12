# Django开发的MTV模型

## model
+ 每个模型都被表示为 django.db.models.Model 类的子类，从它继承了操作数据库需要的所有方法。
+ 每个字段都是 Field 类的实例 。比如字符字段被表示为 CharField ，日期时间字段被表示为 DateTimeField。这将告诉Django要处理的数据类型。
+ 定义某些 Field 类实例需要参数。例如 CharField 需要一个 max_length参数。这个参数的用处不止于用来定义数据库结构，也用于验证数据。
+ 使用 ForeignKey定义一个关系。这将告诉 Django，每个（或多个） ArticlePost 对象都关联到一个 User 对象。

## templates

## views


# django的路由分配



## 开发三件套
+ render:
```
render(request, template_name, context=None, content_type=None, status=None, using=None)
```
+ redirect
```
redirect(to, *args, permanent=False, **kwargs)
```
+ HttpResponse
```
HttpResponse(HttpResponseBase)
```
