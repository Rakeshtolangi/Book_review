from django.shortcuts import render


def index(request):
    name = "Bookr"
    return render(request, 'base.html', {"name": name})