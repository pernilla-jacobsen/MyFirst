from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Cat




def home(request):
    catList = Cat.objects.all()
    return render(request, 'cats/cat_home.html', {"catList":catList})


class CatListView(ListView):
    model = Cat
    template_name = 'cats/cat_home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'catList'
    ordering = ['-date_posted']


class CatDetailView(DetailView):
    model = Cat


class CatCreateView(LoginRequiredMixin, CreateView):
    model = Cat
    fields = ['name', 'age', 'breed', 'favorite_toy', 'picture']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CatDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Cat
    success_url = '/cats/'

    def test_func(self):
        cat = self.get_object()
        if self.request.user == cat.author:
            return True
        return False

class CatUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Cat
    fields = ['name', 'age', 'breed', 'favorite_toy', 'picture']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        cat = self.get_object()
        if self.request.user == cat.author:
            return True
        return False

def about(request):
    return render(request, 'cats/cat_about.html', {'title': 'About'})


""" 
def index(request):
    myCatList = Cat.objects.all()
    
    return HttpResponse(f"Hello, world. You're at the cats index. First cat: {myCatList[0] if myCatList else 'No cats available.'}  ")

 """