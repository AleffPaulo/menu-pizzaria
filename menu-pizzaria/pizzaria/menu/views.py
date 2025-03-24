from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def pizzas_tradicionais(request):
    pizzas = [
        {"id": 1, "Nome": "Marguerita", "Preco": 30},
        {"id": 2, "Nome": "Pepperoni", "Preco": 35},
        {"id": 3, "Nome": "Quatro Queijos", "Preco": 40},
    ]
    bebidas = [
        {"id": 1, "Nome": "Coca-Cola", "Preco": 5},
        {"id": 2, "Nome": "Guarana", "Preco": 5},
        {"id": 3, "Nome": "agua", "Preco": 3},
    ]
    return JsonResponse({"pizzas": pizzas, "bebidas": bebidas})

def pizzas_especiais(request):
    pizzas = [
        {"id": 1, "Nome": "Pizza de Frango com Catupiry", "Preco": 45},
        {"id": 2, "Nome": "Pizza de Calabresa defumada", "Preco": 40},
        {"id": 3, "Nome": "Pizza de Portuguesa", "Preco": 50},
    ]
    bebidas = [
        {"id": 1, "Nome": "Coca-Cola", "Preco": 5},
        {"id": 2, "Nome": "Guarana", "Preco": 5},
        {"id": 3, "Nome": "agua", "Preco": 3},
    ]
    return JsonResponse({"pizzas": pizzas, "bebidas": bebidas})

def sanduiches_tradicionais(request):
    sanduiches = [
        {"id": 1, "Nome": "Sanduíche de Presunto e Queijo", "Preco": 15},
        {"id": 2, "Nome": "Sanduíche de Frango", "Preco": 18},
        {"id": 3, "Nome": "Sanduíche de Atum", "Preco": 20},
    ]
    bebidas = [
        {"id": 1, "Nome": "Coca-Cola", "Preco": 5},
        {"id": 2, "Nome": "Guarana", "Preco": 5},
        {"id": 3, "Nome": "agua", "Preco": 3},
    ]
    return JsonResponse({"sanduiches": sanduiches, "bebidas": bebidas})

def sanduiches_artesanais(request):
    sanduiches = [
        {"id": 1, "Nome": "Sanduíche Artesanal de Carne", "Preco": 25},
        {"id": 2, "Nome": "Sanduíche Artesanal de Frango com requeijao", "Preco": 28},
        {"id": 3, "Nome": "Sanduíche Artesanal Vegano", "Preco": 22},
    ]
    bebidas = [
        {"id": 1, "Nome": "Coca-Cola", "Preco": 5},
        {"id": 2, "Nome": "Guarana", "Preco": 5},
        {"id": 3, "Nome": "agua", "Preco": 3},
    ]
    return JsonResponse({"sanduiches": sanduiches, "bebidas": bebidas})