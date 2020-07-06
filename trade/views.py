from django.shortcuts import render


def list(request):
    return render(request, 'trade/list.html')


def first(request):
    return render(request, 'trade/first.html')


def second(request):
    return render(request, 'trade/second.html')


def third(request):
    return render(request, 'trade/third.html')