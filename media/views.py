from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'wlcm': 'Media page'}
    return render(request, 'media/index.html', context)

