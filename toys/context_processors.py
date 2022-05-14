from .models import Category, Toy


def list_categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return context


def list_toys(request):
    toys = Toy.objects.all()
    context = {'toys': toys}
    return context
