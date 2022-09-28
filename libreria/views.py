import email
from ast import Return
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Motos
from .forms import  MotosForm
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.decorators import login_required

# Create your views here.

# todo lo de paginas
@login_required
def inicio(request):
    return render(request, 'paginas/inicio.html')

def contacto(request):
    return render(request, 'contact/contacto.html')
def contactar(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + " "
        email_desde = settings.EMAIL_HOST_USER
        email_para = [request.POST["txtEmail"]]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "contact/exitoso.html")
    return render(request, "contact/contacto.html")

#todo lo de motos
def motos(request):
    motos = Motos.objects.all()
    return render(request, 'motos/index.html', {'motos':motos})
    
def crear(request):
    formulario = MotosForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('motos')
    return render(request, 'motos/crear.html', {'formulario': formulario})

def editar(request, id):
    motos = Motos.objects.get(id=id)
    formulario = MotosForm(request.POST or None, request.FILES or None, instance=motos)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('motos')
    return render(request, 'motos/editar.html', {'formulario': formulario})

def eliminar(request, id):
    motos = Motos.objects.get(id=id)
    motos.delete()
    return redirect('motos')