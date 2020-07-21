from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Post2

def main(request):
    return render(request, 'accounting/main.html')


def first(request):
    posts = Post.objects.all()
    return render(request, 'accounting/first.html', {'posts':posts})


def second(request):
    posts2 = Post2.objects.all()
    return render(request, 'accounting/second.html', {'posts2':posts2})


def third(request):
    posts = Post.objects.all()
    return render(request,'accounting/third.html', {'posts':posts})


def review(request):
    return render(request,'accounting/review.html')


def review2(request):
    return render(request,'accounting/review2.html')


def create(request):
    if request.method =="POST":
        title = request.POST.get('title')
        reason = request.POST.get('reason')
        base = request.POST.get('base')
        experience = request.POST.get('experience')
        difficulty = request.POST.get('difficulty')
        recommend = request.POST.get('recommend')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        Post.objects.create(image=image, title=title, reason=reason, base=base, experience=experience, difficulty=difficulty, recommend=recommend, content=content)
        return redirect('accounting:first')


def create2(request):
    if request.method =="POST":
        title = request.POST.get('title')
        reason = request.POST.get('reason')
        base = request.POST.get('base')
        experience = request.POST.get('experience')
        difficulty = request.POST.get('difficulty')
        recommend = request.POST.get('recommend')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        Post2.objects.create(image=image, title=title, reason=reason, base=base, experience=experience, difficulty=difficulty, recommend=recommend, content=content)
        return redirect('accounting:second')


def show(request, id):
    post = Post.objects.get(pk=id)
    return render(request,'accounting/show.html', {'post': post})


def update(request,id):
    post = get_object_or_404(Post,pk=id)
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.reason = request.POST['reason']
        post.base = request.POST['base']
        post.experience = request.POST['experience']
        post.difficulty = request.POST['difficulty']
        post.recommend = request.POST['recommend']
        post.image = request.FILES.get('image')
        post.save()
        return redirect('accounting:main')
    return render(request,'accounting/update.html', {'post':post})


def delete(request, id): 
	post = get_object_or_404(Post, pk=id) 
	post.delete()
	return redirect('accounting:main')
