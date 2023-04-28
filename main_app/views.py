from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Wine
from .forms import SoldDateForm

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
    solddate_form = SoldDateForm()
    return render(request, 'wines/detail.html', {'wine':wine, 'solddate_form': solddate_form})

def add_solddate(request, wine_id):
    # create a ModelForm instance using the data in request.POST
    form = (request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_solddate = form.save(commit=False)
        new_solddate.wine_id = wine_id
        new_solddate.save()
    return redirect('detail', wine_id=wine_id)

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