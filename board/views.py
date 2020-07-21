from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def main(request):
    posts = Post.objects.all()
    return render(request, 'board/main.html', {'posts': posts})


def new(request):
    return render(request, 'board/new.html')


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        Post.objects.create(title=title, content=content, image=image)
        return redirect('board:main')


def show(request, id):
    post = Post.objects.get(pk=id)
    return render(request,'board/show.html', {'post': post})


def update(request,id):
    post = get_object_or_404(Post,pk=id)
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.image = request.FILES['image']
        post.save()
        return redirect('board:main')
    return render(request,'board/update.html',{'post':post})


def delete(request, id): 
	post = get_object_or_404(Post, pk=id) 
	post.delete()
	return redirect('board:main')
