from django.http import HttpResponse

from cats.models import Cat



def index(request):
    import random
    all_cats = Cat.objects.all()
    randomCat = random.choice(all_cats) if all_cats else None
    return HttpResponse(f"Hello, world. You're at the myfirst index. Random cat: {randomCat}.")