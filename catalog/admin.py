from django.contrib import admin

from catalog.models import Product, Category, Version


# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_for_one', 'category', 'date_creation',)
    list_filter = ('category', )
    search_fields = ('name', 'description', )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_c')

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('name', 'version_number', 'version_name', 'current', )