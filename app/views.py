from django.shortcuts import render

# Create your views here.
def usdf(request):
    d={'data':'hello Python hi YOU'}
    return render(request,'usdf.html',d)