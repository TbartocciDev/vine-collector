from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Wine

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def wines_index(request):
    wines = Wine.objects.all()
    return render(request, 'wines/index.html', {'wines':wines})

def wines_detail(request,wine_id):
    wine = Wine.objects.get(id=wine_id)
    return render(request, 'wines/detail.html', {'wine':wine})

class WinesCreate(CreateView):
    model = Wine
    fields = '__all__'
    success_url = '/wines/{wine_id}'

class WineUpdate(UpdateView):
    model = Wine
    fields = '__all__'

class WineDelete(DeleteView):
    model = Wine
    success_url = '/wines'