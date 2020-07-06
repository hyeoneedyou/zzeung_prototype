from django.shortcuts import render

def list(request):
    return render(request, 'computer/list.html')


def first(request):
    return render(request, 'computer/first.html')


def second(request):
    return render(request, 'computer/second.html')


def third(request):
    return render(request, 'computer/third.html')