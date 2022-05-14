from django.shortcuts import render, get_object_or_404
from .models import Category, Toy


def details_toy(request, slug):
    toy = get_object_or_404(Toy, slug=slug)
    page = toy.name
    context = {
        'toy': toy,
        'page': page,
    }
    return render(request, 'toys/details_toy.html', context)


def details_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    toys = Toy.objects.filter(category=category)
    page = category.name
    context = {
        'category': category,
        'toys': toys,
        'page': page,
    }
    return render(request, 'toys/details_category.html', context)
