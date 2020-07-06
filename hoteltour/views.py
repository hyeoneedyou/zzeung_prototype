from django.shortcuts import render

def list(request):
    return render(request, 'hoteltour/list.html')


def first(request):
    return render(request, 'hoteltour/first.html')


def second(request):
    return render(request, 'hoteltour/second.html')


def third(request):
    return render(request, 'hoteltour/third.html')