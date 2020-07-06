from django.shortcuts import render


def list(request):
    return render(request, 'chinese/list.html')


def first(request):
    return render(request, 'chinese/first.html')


def second(request):
    return render(request, 'chinese/second.html')


def third(request):
    return render(request, 'chinese/third.html')