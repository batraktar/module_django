from django.shortcuts import render


def prod(request):
    return render(request, 'base.html')
