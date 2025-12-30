from django.shortcuts import HttpResponse

from .models import Cat

def index(request):
    myCatList = Cat.objects.all()
    
    return HttpResponse(f"Hello, world. You're at the cats index. First cat: {myCatList[0] if myCatList else 'No cats available.'}  ")

