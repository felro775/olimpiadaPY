"""
URL configuration for nomo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.paginaweb),
    path('ejemplo1/', views.ejemplo1, name="ejemplo1"),
    path('resultadoe1/', views.resultadoe1, name="resultadoe1"),

    path('macargafron/', views.macargafron, name="macargafron"),
    path('mavolqueta/', views.mavolqueta, name="mavolqueta"),
    path('maexcavado/', views.maexcavado, name="maexcavado"),
    path('mamotonive/', views.mamotonive, name="mamotonive"),
    path('marodillo/', views.marodillo, name="marodillo"),
    path('resultado/', views.resultado, name="resultado"),
