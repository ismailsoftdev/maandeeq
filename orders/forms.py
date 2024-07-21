from django import forms
from django.core.validators import MinValueValidator
from .models import Order, OrderItem
from customers.models import Customer
from products.models import Product

class CustomerSearchForm(forms.Form):
    query = forms.CharField(
        max_length=255,
        label='Search by phone number or name',
        widget=forms.TextInput(attrs={'placeholder': 'Phone number or name', 'class': 'form-control'})
    )


class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['customer', ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class OrderItemForm(forms.ModelForm):
    quantity = forms.IntegerField(validators=[MinValueValidator(1)], initial=1, widget=forms.NumberInput(attrs={'min': 1}))
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


OrderItemFormSet = forms.inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)
