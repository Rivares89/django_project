from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contact/', contact, name='contact')
]