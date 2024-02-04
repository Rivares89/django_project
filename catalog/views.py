from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version, Category
from catalog.services import get_categories_cache


class ProductListView(ListView):
    model = Product
    # template_name = 'catalog/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()[:1]
        for product in products:
            product.active_version = product.version_set.filter(current=True).first()
        context['products'] = products
        return context


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/product_list.html', context)

def categories(request):
    context = {
        'object_list': get_categories_cache(),
        'title': 'Категории'
    }
    return render(request, 'catalog/categories.html', context)

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



class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    # template_name = 'catalog/product_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if settings.CACHE_ENABLED:
            key = f'version_list_{self.object.pk}'
            version_list = cache.get(key)
            if version_list is None:
                version_list = self.object.version_set.all()
                cache.set(key, version_list)
            else:
                version_list = self.object.version_set.all()

        context_data['versions'] = version_list
        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    # fields = ('name', 'description', 'category', 'price_for_one', 'image')
    success_url = reverse_lazy('catalog:list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    # fields = ('name', 'description', 'category', 'price_for_one', 'image')
    success_url = reverse_lazy('catalog:list')
    permission_required = 'catalog.change_product'

    def has_permission(self) -> bool:
        perms = self.get_permission_required()
        if self.request.user.has_perms(perms):
            return True

        product: Product = self.get_object()
        if self.request.user == product.owner:
            return True

        return False

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     if self.object.user != self.request.user:
    #         raise Http404
    #     return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list')
    permission_required = 'catalog.delete_product'
