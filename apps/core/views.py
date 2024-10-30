from apps.store.models import Product
from django.shortcuts import render


# Create your views here.
def frontpage(request):  # noqa: ANN201, D103
    products = Product.objects.all()

    context = {"products": products}

    return render(request, "frontpage.html", context)


def contact(request):
    return render(request, "contact.html")
