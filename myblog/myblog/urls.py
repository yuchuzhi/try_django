"""myblog URL Configuration

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
from django.conf import settings
from django.views.static import serve
from django.urls import path, include, re_path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.home),
    path('', views.index, name='index'),
    path('blog/article', views.article),
    path('blog/show', views.show),
    path('blog/edit', views.edit),
    path('blog/search', views.search),
    path('blog/comment', views.comment),
    path('blog/list-<int:lid>.html', views.list, name='list'),#列表页
    path('blog/show-<int:sid>.html', views.show, name='show'),#内容页
    path('blog/tag/<tag>', views.tag, name='tags'),#标签列表页
    path('blog/s/', views.search, name='search'),#搜索列表页
    path('blog/about/', views.about, name='about'),#联系我们单页
    path('ueditor/', include('DjangoUeditor.urls')),
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
