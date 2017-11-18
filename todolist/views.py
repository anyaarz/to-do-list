from django.shortcuts import render, render_to_response,redirect, get_object_or_404
from django.http.response import HttpResponse,Http404
from .models import Article
from django.core.exceptions import ObjectDoesNotExist
from .forms import ArticleForm
from django.template.context_processors import csrf
from django.utils import timezone



def header_page(request):
    return render_to_response('todolist/header_page.html',)

def articles(request):
    return render_to_response('todolist/main.html',{'articles':Article.objects.all()})

def post_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.published_date = timezone.now()
            form.save()
            return redirect('/articles/all/')
    else:
        form = ArticleForm()
    return render(request, 'todolist/post_edit.html', {'form': form})

def post_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.published_date = timezone.now()
            form.save()
            return redirect('/articles/all/')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'todolist/post_edit.html', {'form': form})

def post_delete(request, pk):
        article = Article.objects.get (pk = pk)
        article.delete()
        return redirect('/articles/all/')

# Create your views here.
