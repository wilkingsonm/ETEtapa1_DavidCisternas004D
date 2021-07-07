from .forms import ColabForm
from .models import Colabreg
from django.shortcuts import redirect, render


def index(request):

    return render(request, 'index.html',
    )


def login(request):

    return render(request, 'core/login.html',
    )


def registroo(request):
    colabor = Colabreg.objects.all()
    if request.method == 'POST': 

        colab_form = ColabForm(request.POST)

        if colab_form.is_valid():

            colab_form.save()       

            return redirect('index')

    else: 

        colab_form = ColabForm()

    return render(request, 'core/registroo.html', {'colab_form': colab_form, 'colab': colabor})

def Ver(request):
    colabo = Colabreg.objects.all()

    return render(request, 'core/ver.html', context={'colaboradores':colabo})