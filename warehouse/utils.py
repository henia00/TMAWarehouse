def filter_items(items, filter_form):
    if filter_form.cleaned_data['item_group']:
        items = items.filter(item_group=filter_form.
                             cleaned_data['item_group'])
    if filter_form.cleaned_data['unit_of_measurement']:
        items = items.filter(unit_of_measurement=filter_form.
                             cleaned_data['unit_of_measurement'])
    if filter_form.cleaned_data['min_quantity']:
        items = items.filter(quantity__gt=filter_form.
                             cleaned_data['min_quantity'])
    if filter_form.cleaned_data['max_quantity']:
        items = items.filter(quantity__lt=filter_form.
                             cleaned_data['max_quantity'])
    if filter_form.cleaned_data['min_price']:
        items = items.filter(price_without_vat__gt=
                             filter_form.cleaned_data['min_price'])
    if filter_form.cleaned_data['max_price']:
        items = items.filter(price_without_vat__lt=
                             filter_form.cleaned_data['max_price'])
    return items


def filter_orders(orders, filter_form):
    if filter_form.cleaned_data['employee_name']:
        orders = orders.filter(employee_name=filter_form.
                               cleaned_data['employee_name'])
    if filter_form.cleaned_data['order_status']:
        orders = orders.filter(order_status=filter_form.
                               cleaned_data['order_status'])
    return orders


def search_items(items, search_form):
    items = items.filter(item_name=search_form.cleaned_data['name_to_search'])
    return items


def search_orders(orders, search_orders_form):
    orders = orders.filter(request_id=search_orders_form.
                           cleaned_data['id_to_search'])
    return orders