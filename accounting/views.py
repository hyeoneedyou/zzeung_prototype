from django.shortcuts import render

def list(request):
    return render(request, 'accounting/list.html')


def first(request):
    return render(request, 'accounting/first.html')


def second(request):
    return render(request, 'accounting/second.html')


def third(request):
    return render(request, 'accounting/third.html')
