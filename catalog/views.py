from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from catalog.models import Product



class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'category', 'price_for_one',)
    success_url = reverse_lazy('catalog:form')

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/catalog_list.html'

def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/catalog_list.html', context)

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



class ProductDetailView(DetailView):
    model = Product



