from django.shortcuts import render,redirect

wines = [
  {
    'name':'13 Celsius',
    'abv': 12.5,
    'region':'Italy',
    'dryness':'Dry',
    'size':'750ML',
    'type':'Sauvignon Blanc',
    'color':'White'
   },
   {
    'name':'19 Crimes',
    'abv': 13.5,
    'region':'Australia',
    'dryness':'Sweet',
    'size':'750ML',
    'type':'Pinot Noir',
    'color':'Red'
   },
   {
    'name':'7 Deadly',
    'abv': 14,
    'region':'United States',
    'dryness':'Dry',
    'size':'750ML',
    'type':'Cabernet Sauvignon',
    'color':'Red'
   },
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def wines_index(request):
    return render(request, 'wines/index.html', {'wines':wines})