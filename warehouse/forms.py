from django.forms import ModelForm
from django import forms
from .models import Items, Order, OrderItem


UNITS_OF_MEASUREMENT = (
    (None, '---'),
    ('0', 'UNIT0'),
    ('1', 'UNIT1'),
    ('2', 'UNIT2')
)
ITEM_GROUPS = (
    (None, '---'),
    ('0', 'GROUP0'),
    ('1', 'GROUP1'),
    ('2', 'GROUP2')
)
ORDER_STATUS_CHOICE = (
    (None, '---'),
    ('New', 'New'),
    ('Accepted', 'Accepted'),
    ('Declined', 'Declined')
)

class ItemsForm(ModelForm):
    """ Form based on the model Item. """
    class Meta:
        model = Items
        fields = ['item_name', 'item_group', 'unit_of_measurement',
                  'quantity', 'price_without_vat', 'status',
                  'storage_location', 'contact_person', 'photo']


class OrderForm(forms.Form):
    """ Form to create a new order. """
    employee_name = forms.CharField(max_length=100)
    item_name = forms.ModelChoiceField(queryset=Items.objects.all(), empty_label=None)
    unit = forms.ChoiceField(choices=UNITS_OF_MEASUREMENT)
    quantity = forms.IntegerField()
    price_without_vat = forms.FloatField()
    comment = forms.CharField(max_length=1000, required=False)


class AddToOrderForm(forms.Form):
    """ Form to add new request to the existing order. """
    item_name = forms.ModelChoiceField(queryset=Items.objects.all(), empty_label=None)
    unit = forms.ChoiceField(choices=UNITS_OF_MEASUREMENT)
    quantity = forms.IntegerField()
    price_without_vat = forms.FloatField()


class DeclinedForm(forms.Form):
    """ Form to get comment in the case of declining the order. """
    comment = forms.CharField(widget=forms.Textarea(attrs={"rows": "5"}))


class ItemFilterForm(forms.Form):
    """ Form to filter items """
    item_group = forms.ChoiceField(choices=ITEM_GROUPS, required=False)
    unit_of_measurement = forms.ChoiceField(choices=UNITS_OF_MEASUREMENT,
                                            required=False)
    min_quantity = forms.IntegerField(label='Minimum Quantity', required=False)
    max_quantity = forms.IntegerField(label='Maximum Quantity', required=False)
    min_price = forms.FloatField(label='Mimimum Price (without VAT)',
                                 required=False)
    max_price = forms.FloatField(label='Maximum Price (without VAT)',
                                 required=False)


class OrderFilterForm(forms.Form):
    """ Form to filter orders """
    employee_name = forms.CharField(max_length=100, required=False)
    order_status = forms.ChoiceField(choices = ORDER_STATUS_CHOICE,
                                     required=False)


class SearchItemForm(forms.Form):
    name_to_search = forms.CharField(max_length=50, label="Item's name to search", required=True)


class SearchOrderForm(forms.Form):
    id_to_search = forms.IntegerField(label="Order's ID to search", required=True)