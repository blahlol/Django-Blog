from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from articles.models import Article
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save() #this returns the user automatically so dont need to call form.get_user again
            login(request,user)
            return redirect('accounts:login')
    else:
        form=UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form}) #this is outside the else because we need to render this for a get request and for when the form in not valid.

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list',type='all')
        else:
            return render(request,'accounts/login.html',{'form':form})
    else:
        if request.user.username=='':
            form=AuthenticationForm()
            return render(request,'accounts/login.html',{'form':form})
        else:
            return redirect('articles:list',type='all')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')


# @login_required(login_url='accounts:login')
# def find(request,value):
#     objects=list(User.objects.filter(username__contains=value).values('username','id'))
#     return JsonResponse(objects,safe=False)

@login_required(login_url='accounts:login')
def profile(request,id):
    articles=Article.objects.filter(author=id).order_by('-date')
    for article in articles:
        if len(article.likes_set.filter(person=request.user))==1:
            article.status='Liked'
        elif len(article.likes_set.filter(person=request.user))==0:
            article.status='Like'
    user=User.objects.get(id=id)
    context={'user':user,'articles':articles,'length':len(articles)}
    if int(id)==request.user.id:
        context['self']=True
    return render(request,'accounts/profile.html',context)
