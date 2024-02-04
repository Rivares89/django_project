from django import forms

from catalog.models import Product, Version

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

ERROR_NANE = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price_for_one', 'image',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        if cleaned_data in ERROR_NANE:
            raise forms.ValidationError('Такой продукт нельзя добавить')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ('name', 'version_number', 'version_name', 'current',)
