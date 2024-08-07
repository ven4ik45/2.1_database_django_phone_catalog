from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_objects = Phone.objects.all()
    sort_filter = request.GET.get('sort', '')
    context = {'phones': phone_objects}

    match sort_filter:
        case "name":
            context = {'phones': phone_objects.order_by('name')}
        case "min_price":
            context = {'phones': phone_objects.order_by('price')}
        case "max_price":
            context = {'phones': phone_objects.order_by('-price')}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
