from django.db import models

UNITS_OF_MEASUREMENT = (
    ('0', 'UNIT0'),
    ('1', 'UNIT1'),
    ('2', 'UNIT2')
)
ITEM_GROUPS = (
    ('0', 'GROUP0'),
    ('1', 'GROUP1'),
    ('2', 'GROUP3')
)


class Items(models.Model):
    """
    Model for storing data related to individual items.

    Attributes:
        item_id (AutoField): Primary key for the item.
        item_name (CharField): Name of the item. Maximum length is 50 characters. Must be unique.
        item_group (CharField): Group to which the item belongs, chosen from predefined choices.
        unit_of_measurement (CharField): Unit of measurement for the item, chosen from predefined choices.
        quantity (IntegerField): Quantity of the item.
        price_without_vat (FloatField): Price of the item without VAT.
        status (CharField): Status of the item.
        storage_location (CharField): Location where the item is stored (optional).
        contact_person (TextField): Contact person related to the item (optional).
        photo (ImageField): Image of the item (optional).
    """
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50, unique=True, blank=False,
                                 default='None')
    item_group = models.CharField(max_length=50, choices=ITEM_GROUPS,
                                  default='0')
    unit_of_measurement = models.CharField(max_length=50,
                                           choices=UNITS_OF_MEASUREMENT,
                                           default='0')
    quantity = models.IntegerField()
    price_without_vat = models.FloatField(blank=False)
    status = models.CharField(max_length=300, blank=False)
    storage_location = models.CharField(max_length=300, blank=True, null=True)
    contact_person = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True,null=True)

    def __str__(self):
        return str(self.item_name)


class Order(models.Model):
    """
    Model for storing data related to individual orders.

    Attributes:
        request_id (AutoField): Primary key for the order.
        employee_name (CharField): Name of the employee. Maximum length is 100 characters.
        comment (TextField): Field to provide any comment (optional).
        status (CharField): Status of the order.
    """
    request_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    comment = models.TextField(blank=True)
    order_status = models.CharField(max_length=20, default='New')



class OrderItem(models.Model):
    """
    Model for storing data of individual request, which are part of the order.

    Attributes:
        order (ForeignKey): The order to which the request belongs.
        row_id (AutoField): Primary key for the individual request.
        item_name (ForeignKey): The name of the item which is requested.
        unit_of_measurement (CharField): Unit of measurement for the item, chosen from predefined choices.
        quantity (IntegerField): Quantity of the item.
        price_without_vat (FloatField): Price of the item without VAT.

    """
    order = models.ForeignKey(Order, related_name='order',
                              on_delete=models.CASCADE, default=None)
    row_id = models.AutoField(primary_key=True)
    item_name = models.ForeignKey(Items, on_delete=models.CASCADE)
    unit = models.CharField(max_length=50, choices=UNITS_OF_MEASUREMENT,
                            default='0')
    quantity = models.IntegerField()
    price_without_vat = models.FloatField()


