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
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50, unique=True, blank=False, default='None')
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
    request_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    comment = models.TextField(blank=True)
    order_status = models.CharField(max_length=20, default='New')



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE, default=None)
    row_id = models.AutoField(primary_key=True)
    item_name = models.ForeignKey(Items, on_delete=models.CASCADE)
    unit = models.CharField(max_length=50, choices=UNITS_OF_MEASUREMENT, default='0')
    quantity = models.IntegerField()
    price_without_vat = models.FloatField()


