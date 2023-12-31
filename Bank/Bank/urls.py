"""
URL configuration for Bank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import RedirectView
from django.urls import path
from cards import views as v_cards
from main import views as v_main
from login import views as v_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cards/', v_cards.cards, name='cards'),
    path('', RedirectView.as_view(url='main')),
    path('main/', v_main.main, name='main'),
    path('login/', v_login.login, name='login')
]
