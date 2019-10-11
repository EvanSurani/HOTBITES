from django import forms
from adminside.models import addproductcat

class add_product_cat(forms.ModelForm):
    product_name = forms.CharField(max_length = 20)
    category = forms.CharField(max_length = 20)

    