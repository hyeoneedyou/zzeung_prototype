from django.shortcuts import render

def main(request):
    return render(request, 'english/main.html')


def first(request):
    return render(request, 'english/first.html')


def second(request):
    return render(request, 'english/second.html')


def third(request):
    return render(request, 'english/third.html')
