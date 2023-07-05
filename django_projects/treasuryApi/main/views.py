from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def accounting(request, pk):
    return render(request, 'accounting.html')
