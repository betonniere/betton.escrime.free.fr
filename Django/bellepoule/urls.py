"""bellepoule URL Configuration

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
"""
# On remplace django.conf.urls par django.urls
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    # Utilisation de path() au lieu de url()
    # Notez que l'on retire le préfixe r'^' et le suffixe '/' final est géré plus simplement
    path('admin/', admin.site.urls),
    path('fencing-tournament-software/', include('website.urls')),
]
