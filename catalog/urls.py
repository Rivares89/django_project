from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import contact, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, categories

app_name = CatalogConfig.name

urlpatterns = [
    # path('', cache_page(60)(ProductListView.as_view()), name='list'),
    path('', ProductListView.as_view(), name='list'),
    path('categories/', categories, name='categories'),
    path('view/<int:pk>/', cache_page(60)(ProductDetailView.as_view()) , name='view'),
    path('contact/', contact, name='contact'),

    # path('create/', ProductCreateView.as_view(), name='create'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    # path('edit/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),


    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
]