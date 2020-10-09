from django.shortcuts import render


# Create your views here.
def home(request):
    html = 'home.html'
    context = {
        "Welcome": "Welcome to my blog."
    }
    return render(request, html, context=context)


def article(request):
    html = 'Hello World!'
    return render(request, html, {})


def show(request):
    html = 'Hello World!'
    return render(request, html, {})


def edit(request):
    html = 'Hello World!'
    return render(request, html, {})


def search(request):
    html = 'Hello World!'
    return render(request, html, {})


def comment(request):
    html = 'Hello World!'
    return render(request, html, {})

