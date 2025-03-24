from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pizzas/tradicionais/', views.pizzas_tradicionais, name='pizzas_tradicionais'),
    path('pizzas/especiais/', views.pizzas_especiais, name='pizzas_especiais'),
    path('sanduiches/tradicionais/', views.sanduiches_tradicionais, name='sanduiches_tradicionais'),
    path('sanduiches/artesanais/', views.sanduiches_artesanais, name='sanduiches_artesanais'),
]