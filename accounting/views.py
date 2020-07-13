from django.shortcuts import render, redirect
from .models import Post

def list(request):
    return render(request, 'accounting/list.html')


def first(request):
    posts = Post.objects.all()
    return render(request, 'accounting/first.html', {'posts':posts})


def second(request):
    posts = Post.objects.all()
    return render(request, 'accounting/second.html', {'posts':posts})


def third(request):
    posts = Post.objects.all()
    return render(request,'accounting/third.html', {'posts':posts})


def review(request):
    return render(request,'posts/review.html')


def create(request):
    if request.method =="POST":
        title = request.POST.get('title')
        reason = request.POST.get('reason')
        base = request.POST.get('base')
        experience = request.POST.get('experience')
        difficulty = request.POST.get('difficulty')
        recommend = request.POST.get('recommend')
        content = request.POST.get('content')
        Post.objects.create(title=title, reason=reason, base=base, experience=experience, difficulty=difficulty, recommend=recommend, content=content)
        return redirect('accounting:list')


def show(request, id):
    post = Post.objects.get(pk=id)
    return render(request,'accounting/show.html', {'post': post})