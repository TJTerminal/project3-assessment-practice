from django.shortcuts import render
from .models import Toy
from django.views.generic.edit import CreateView, DeleteView

def index(request):
    toys = Toy.objects.all()
    return render(request, 'index.html', { 'toys': toys })

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'
    success_url = '/'

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/'