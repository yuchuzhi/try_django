from django.contrib import admin

from .models import Article, Category


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'views', 'tui', 'user', 'body', 'created_time', 'modify_time') # 'tui', 'user', 'views',
    # 文章列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-created_time',)
    #后台数据列表排序方式
    list_display_links = ('id', 'title')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')

