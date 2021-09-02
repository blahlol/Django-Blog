from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.views import generic
from django.http import JsonResponse
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
@login_required(login_url="accounts:login")
def article_list(request,type):
    context=dict()
    if request.user.is_superuser:
        if type=='all':articles=Article.objects.filter(approved=True).order_by('-date')
        elif type=='pending':
            articles=Article.objects.filter(approved=False).order_by('-date')
            context['pending']=True
    else:
        articles=Article.objects.filter(approved=True).order_by('-date')
    for article in articles:
        if len(article.likes_set.filter(person=request.user))==1:
            article.status='Liked'
        elif len(article.likes_set.filter(person=request.user))==0:
            article.status='Like'
    context['articles']=articles
    context['user']=request.user
    return render(request,'articles/article_list.html',context)

@login_required(login_url="accounts:login")
def article_create(request):
    if request.method=='POST':
        form=forms.CreateArticle(request.POST,request.FILES) #request.FILES is used only when we have a file upload in our form
        if form.is_valid():
            instance=form.save(commit=False) #commit false saves but doesnt commit
            instance.author=request.user #to    set the author to the person who is logged in
            if request.user.is_superuser:
                instance.approved=True
            instance.save() #finally save
            return redirect('articles:list',type='all')

    else:
        form=forms.CreateArticle()
        return render(request,'articles/article_create.html',{'form':form})

@login_required(login_url='accounts:login')
def article_delete(request,id):
    tbd=Article.objects.get(id=id)
    tbd.delete()
    return redirect('articles:list',type='all')

@login_required(login_url='accounts:login')
def article_edit(request,id):
    if request.method=='POST':
        obj=Article.objects.get(id=id)
        form=forms.CreateArticle(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
        return redirect('articles:list',type='all')
    else:
        obj=Article.objects.get(id=id)
        form=forms.CreateArticle(instance=obj)
        return render(request,'articles/article_edit.html',{'form':form,'id':id})

@login_required(login_url='accounts:login')
def article_like(request,id):
    article=Article.objects.get(id=id)
    if len(article.likes_set.filter(person=request.user))==1:
        delete=article.likes_set.get(person=request.user)
        delete.delete()
        article.no_of_likes-=1
        article.save()

    elif len(article.likes_set.filter(person=request.user))==0:
        article.likes_set.create(person=request.user)
        article.no_of_likes+=1
        article.save()
    return JsonResponse({'likes':article.no_of_likes})

@login_required(login_url='accounts:login')
def article_comment(request,id):
    article=Article.objects.get(id=id)
    return render(request,'articles/comments.html',{'article':article})

@login_required(login_url='accounts:login')
def article_add_comment(request,id,comment):
    article=Article.objects.get(id=id)
    article.comments_set.create(person=request.user,text=comment)
    return HttpResponse('Added')

@login_required(login_url='accounts:login')
def approve(request,status,id):
    article=Article.objects.get(id=id)
    if status=='yes':
        article.approved=True
        article.time=timezone.now()
        article.save()
    elif status=='no':
        article.delete()
    return redirect('articles:list',type='pending')

# def article_detail(request,id):
#     article=Article.objects.get(id=id)
#     return render(request,'articles/article_detail.html',{'article':article})

#same as the above function but used a DetailView (a type of generic view)
# class ArticleDetail(generic.DetailView):
#     template_name='articles/article_detail.html'
#     model=Article
#     context_object_name='article'
