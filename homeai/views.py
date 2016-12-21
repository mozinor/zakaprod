from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'title': "ZAKAZAKA MUSIC", 'sub_title': "Best Songs, Videos, Productions."}
    return render(request, 'homeai/index.html', context)

