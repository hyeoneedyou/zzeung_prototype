from django.shortcuts import render

def list(request):
    return render(request, 'japanese/list.html')


def first(request):
    return render(request, 'japanese/first.html')


def second(request):
    return render(request, 'japanese/second.html')


def third(request):
    return render(request, 'japanese/third.html')