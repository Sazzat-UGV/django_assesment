from django import forms
from .models import Product

class ProductFroms(forms.ModelForm):
    class Meta:
        model=Product
        fields=[
            "name",
            "details",
            "price",
        ]