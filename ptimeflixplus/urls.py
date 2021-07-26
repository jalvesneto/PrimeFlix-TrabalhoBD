"""ptimeflixplus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
app_name = "Primeflix"

from django.contrib import admin
from django.urls import path
from Primeflix.views import addFilme, addEp, addSerie, delete, deleteep, loginUsuario, main, series, cadUsuario, update, updateEp, verTtulos, viewTitulo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginUsuario),
    path('telaCadastrar', cadUsuario),
    path('main', main, name='main'),
    path('addFilme', addFilme),
    path('addSerie', addSerie),
    path('addEp/<int:pk>', addEp, name='addEp'),
    path('series', series, name='series'),
    path('verTitulos', verTtulos, name='verTitulos'),
    path('delete/<int:pk>', delete),
    path('deleteep/<int:pk>/<int:fk>', deleteep),
    path('edit/<int:pk>', update),
    path('editep/<int:pk>/<int:fk>', updateEp),
    path('view/<int:pk>', viewTitulo, name='viewtTitulo') 
]