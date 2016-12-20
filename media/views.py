from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'title': 'ZakaZaka Music'}
    return render(request, 'media/index.html', context)

