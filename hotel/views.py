from django.shortcuts import render, HttpResponse
from .models import Hotel, Quarto, Usuario
from .forms import FormNome 

def reservas(request):
    if request.method == 'POST':
        form = FormNome(request.POST)
        if form.is_valid():

            var_nome = form.cleaned_data['nome']          # pega o nome do form
            var_email = form.cleaned_data['email']        # pega o email do form
            var_idade = form.cleaned_data['idade']        # pega a idade do form
            var_data = form.cleaned_data['data']          # pega a data do form

            print(var_nome, var_email, var_idade, var_data)


            usuario = Usuario(nome=var_nome, email=var_email, idade=var_idade, data=var_data) # cria um objeto do tipo Usuario
            usuario.save() # salva o objeto no banco de dados

            return HttpResponse('<h1>thanks</h1>')
    else:
        form = FormNome()
        return render(request, 'reservas.html', {'form': form})


def homepage(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    return render(request,'homepage.html', context)

def quartos(request):
    context = {}
    dados_quarto = Quarto.objects.all()
    context["dados_quarto"] = dados_quarto
    return render(request,'quartos.html', context)

# def reservas(request):
#     context = {}
#     dados_reserva = Usuario.objects.all()
#     dados_quarto = Quarto.objects.all()
#     context["dados_reserva"] = dados_reserva
#     context["dados_quarto"] = dados_quarto
#     return render(request,'reservas.html', context)

