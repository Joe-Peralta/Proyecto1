"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto1.view import saludo, segunda_vista, template_2, tercera_vista, ano_nacimiento,template_1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/',saludo),
    path('fecha/', segunda_vista),
    path('persona/<nombre>', tercera_vista),
    path('edad/<int:edad>',ano_nacimiento ),
    path('template/',template_1),
    path('template2/<str:nombre>/<int:edad>',template_2)
]
