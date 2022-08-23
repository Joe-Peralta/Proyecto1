
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def saludo(request):
    #logica de Programacion
    return HttpResponse("hola, te saludo desde Django")


def segunda_vista(request):
    ahora = datetime.now()
    mensaje = f'esta es mi segunda vista y fue ejecutada el {ahora}'
    return HttpResponse(mensaje)


def tercera_vista(request,nombre):
    mensaje = f'Hola {nombre}, bienvenido a nuestra plataforma'
    return HttpResponse(mensaje)


def ano_nacimiento(request,edad):
    ano = datetime.now().year - edad
    return HttpResponse(f'naciste en el año {ano}')



def template_1(request):
    contexto = {
        'nombre' : 'joel',
        'edad'   :  32
    }
    return render(request,'template1.html', contexto)


def template_2(request, nombre, edad):
    contexto = {
        'nombre' : nombre,
        'edad'   :  edad,
        'horaactual'  : datetime.now(),
        'lista'  :  [1, 2, 3, 4, 5],
        'diccionario' : {'Animal':"Perro"}
    }
    return render(request,'template1.html', contexto)