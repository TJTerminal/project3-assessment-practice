from django.shortcuts import render
from .models import Toy
from django.views.generic.edit import CreateView

def index(request):
    # toys = Toy.objects.all()
    return render(request, 'index.html')

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'
    success_url = '/'