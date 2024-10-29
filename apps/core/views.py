from apps.store.models import Category, Product
from django.shortcuts import render


# Create your views here.
def frontpage(request):
    products = Product.objects.all()

    context = {"products": products}

    return render(request, "frontpage.html", context)


def contact(request):
    return render(request, "contact.html")
