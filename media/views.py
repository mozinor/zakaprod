from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'title': 'ZakaZaka Production'}
    return render(request, 'media/index.html', context)

