from django.shortcuts import render
from .models import Article     # 명시적 상대경로


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # #1
    # article = Article()
    # article.title = title  
    # article.content = content
    # article.save()

    #2
    article = Article(title=title, content=content)
    article.save()

    #3
    # Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')


def detail(request, pk):
    pass


def delete(request, pk):
    pass


def edit(request, pk):
    pass


def update(request, pk):
    pass
