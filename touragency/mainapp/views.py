from django.http import HttpResponse
from django.shortcuts import render

from mainapp.models import Brand, Collection

# Create your views here.


def main(request) -> HttpResponse:
    """Main page function based controller"""
    title = 'Главная страница'
    brands = Brand.objects.all()
    context = {
        'title': title,
        'brands': brands
    }
    return render(
        request, 'mainapp/index.html', context=context
    )


def brand(request, brand_id: int) -> HttpResponse:
    """View for brands collections"""
    brand_item = Brand.objects.get(pk=brand_id)
    title = brand_item.title
    context = {
        'title': title,
        'brand_item': brand_item
    }
    return render(
        request, 'mainapp/brand.html', context
    )


def collection_view(request, pk: int) -> HttpResponse:
    """View of single collection"""
    collection = Collection.objects.filter(pk=pk).first()
    title = collection.title
    context = {
        'title': title,
        'collection': collection
    }
    return render(
        request, 'mainapp/collection.html', context
    )
