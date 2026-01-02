from django.shortcuts import render

from .models import Cat




def home(request):
    catList = Cat.objects.all()
    return render(request, 'cats/cat_home.html', {"catList":catList})


def about(request):
    return render(request, 'cats/cat_about.html', {'title': 'About'})


""" 
def index(request):
    myCatList = Cat.objects.all()
    
    return HttpResponse(f"Hello, world. You're at the cats index. First cat: {myCatList[0] if myCatList else 'No cats available.'}  ")

 """