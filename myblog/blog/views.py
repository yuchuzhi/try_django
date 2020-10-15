from django.shortcuts import render

from .models import Article, Category, Banner, Tag


# Create your views here.
def home(request):
    html = 'blog/home.html'

    articles = Article.objects.all()
    context = {
        "title": "Z-Blog",
        "articles": articles
    }
    return render(request, html, context=context)


def index(request):
    html = 'blog/index.html'

    categorys = Category.objects.all()
    banner = Banner.objects.filter(is_active=True)[0:4]
    tui = Article.objects.filter(tui__id=1)[:3]
    allarticle = Article.objects.all().order_by('-id')

    context = {
        "title": "Z-Blog",
        "categorys": categorys,
        "banner": banner,
        "tui": tui,
        "allarticle": allarticle,
    }

    return render(request, html, context=context)


def list(request, lid):
    list = Article.objects.filter(category_id=lid)#获取通过URL传进来的lid，然后筛选出对应文章
    cname = Category.objects.get(id=lid)#获取当前文章的栏目名
    remen = Article.objects.filter(tui__id=2)[:2]#右侧的热门推荐
    allcategory = Category.objects.all()#导航所有分类
    tags = Tag.objects.all()#右侧所有文章标签
    return render(request, 'list.html', locals())

def show(request,sid):
    pass


def tag(request, tag):
    pass


def search(request):
    pass


def about(request):
    pass


def article(request):
    html = 'Hello World!'
    return render(request, html, {})


def edit(request):
    html = 'Hello World!'
    return render(request, html, {})


def comment(request):
    html = 'Hello World!'
    return render(request, html, {})

