---
**关关雎鸠，在河之洲。窈窕淑女，君子好逑。**

参差荇菜，左右流之。窈窕淑女，寤寐求之。

---
+ 列表一
+ 列表二
    + 列表二-1
    + 列表二-2
---

```python
def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    # 将markdown语法渲染成html样式
    article.body = markdown.markdown(article.body,
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        ])
    context = { 'article': article }
    return render(request, 'article/detail.html', context)
```