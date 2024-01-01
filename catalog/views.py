from django.shortcuts import render

from catalog.models import Product


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная'
    }

    return render(request, 'catalog/home.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contact.html', context)




