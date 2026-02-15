from django.urls import path, re_path
from . import views

urlpatterns = [
    # Utilisation de path pour la racine (plus simple)
    path('', views.display_page, name='home_page'),

    # Utilisation de re_path pour conserver vos expressions régulières
    # On remplace url(...) par re_path(...)
    re_path(r'^(?P<locale>[a-z]{2})/(?P<pk>.*)/$', views.display_page, name='n_page'),
]
