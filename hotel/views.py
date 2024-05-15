from django.shortcuts import render, HttpResponse
from .models import Hotel, Quarto
# Create your views here.
def homepage(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    return render(request,'homepage.html', context)

def continueHomepage(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    return render(request,'continueHomepage.html', context)

def quartos(request):
    context = {}
    dados_quarto = Quarto.objects.all()
    context["dados_quarto"] = dados_quarto
    return render(request,'quartos.html', context)
