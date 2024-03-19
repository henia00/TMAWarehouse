from django.shortcuts import render, redirect
from .models import Items, Order, OrderItem
from .forms import (ItemsForm, OrderForm, DeclinedForm, ItemFilterForm,
                    SearchItemForm, OrderFilterForm, SearchOrderForm,
                    AddToOrderForm)
from django.contrib import messages
from .utils import filter_items, filter_orders, search_items, search_orders


def home(request):
    """ Home page for employee
    Shows list of items, allows sorting, filtering, and searching
    """
    sort_by = request.GET.get('sort_by', 'item_id')

    if sort_by in [attr for attr in Items.__dict__]:
        items = Items.objects.order_by(sort_by)
    else:
        items = Items.objects.all()

    if 'filter' in request.GET:
        filter_form = ItemFilterForm(request.GET)
        if filter_form.is_valid():
            items = filter_items(items, filter_form)
    else:
        filter_form = ItemFilterForm()

    if 'search_id' in request.GET:
        search_form = SearchItemForm(request.GET)
        if search_form.is_valid():
            items = search_items(items, search_form)
    else:
        search_form = SearchItemForm()

    context = {
        'items': items,
        'title': 'Employee',
        'filter_form': filter_form,
        'search_form': search_form
    }
    return render(request, template_name='warehouse/home.html', context=context)


def coordinator(request):
    """ Coordinator page
    Shows list of items, allows sorting, filtering, and searching
    Shows list of orders, allows sorting, filtering, and searching
    """
    sort_by = request.GET.get('sort_by', 'item_id')
    if sort_by in [attr for attr in Items.__dict__]:
        items = Items.objects.order_by(sort_by)

    if 'filter' in request.GET:
        filter_form = ItemFilterForm(request.GET)
        if filter_form.is_valid():
            items = filter_items(items, filter_form)
    else:
        filter_form = ItemFilterForm()

    if 'search_name' in request.GET:
        search_form = SearchItemForm(request.GET)
        if search_form.is_valid():
            items = search_items(items, search_form)
    else:
        search_form = SearchItemForm()

    sort_request_by = request.GET.get('sort_request_by', 'request_id', )
    if sort_request_by in [attr for attr in Order.__dict__]:
        orders = Order.objects.order_by(sort_request_by)
    else:
        orders = Order.objects.all()

    if 'filter_order' in request.GET:
        filter_order_form = OrderFilterForm(request.GET)
        if filter_order_form.is_valid():
            orders = filter_orders(orders, filter_order_form)
    else:
        filter_order_form = OrderFilterForm()

    if 'search_orders_id' in request.GET:
        search_orders_form = SearchOrderForm(request.GET)
        if search_orders_form.is_valid():
            orders = search_orders(orders, search_orders_form)
    else:
        search_orders_form = SearchOrderForm()

    context = {
        'items': items,
        'orders': orders,
        'title': 'Coordinator',
        'filter_form': filter_form,
        'filter_order_form': filter_order_form,
        'search_form': search_form,
        'search_orders_form': search_orders_form
    }
    return render(request, template_name='warehouse/coordinator.html', context=context)


def add_item(request):
    """ Adding item to items (access from coordinator page) """
    if request.method == "POST":
        form = ItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coordinator')
        context = {'form': form}
    else:
        form = ItemsForm()
        context = {'form': form}
    return render(request, template_name='warehouse/add_item.html',
                  context=context)


def modify_item(request):
    """ Modifying item from items (access from coordinator page) """
    id_to_modify = request.GET.get('item_id')
    item = Items.objects.get(item_id=id_to_modify)
    if request.method == "POST":
        form = ItemsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('coordinator')
    else:
        current_values = {
            'item_id': item.item_id,
            'item_group': item.item_group,
            'unit_of_measurement': item.unit_of_measurement,
            'quantity': item.quantity,
            'price_without_vat': item.price_without_vat,
            'status': item.status,
            'storage_location': item.storage_location,
            'contact_person': item.contact_person,
            'photo': item.photo
        }
        form = ItemsForm(instance=item, initial=current_values)
        context = {'form': form}
    return render(request, template_name='warehouse/modify_item.html', context=context)


def delete_item(request):
    """ Deleting item from items (access from coordinator page) """
    id_to_delete = request.POST.get('item_id')
    Items.objects.filter(item_id = id_to_delete).delete()
    return redirect('coordinator')


def delete_order(request):
    """ Deleting order from orders (access from coordinator page) """
    id_to_delete = request.POST.get('request_id')
    Order.objects.filter(request_id = id_to_delete).delete()
    return redirect('coordinator')


def add_order(request):
    """ Adding new order (access from employee page) """
    if request.method == "POST":
        form = OrderForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            order = Order.objects.create(
                employee_name=form.cleaned_data['employee_name'],
                comment=form.cleaned_data['comment'],
                order_status='New'
            )
            item = Items.objects.get(item_name=form.cleaned_data['item_name'])
            order_item = OrderItem.objects.create(
                order=order,
                item_name=form.cleaned_data['item_name'],
                unit=form.cleaned_data['unit'],
                quantity=form.cleaned_data['quantity'],
                price_without_vat=form.cleaned_data['price_without_vat']
            )
        return redirect('home')
    else:
        form = OrderForm()
        context = {'form': form}
    return render(request, template_name='warehouse/add_order.html',
                  context=context)

def add_to_last_order(request):
    """ Adding to the last order (access from employee page) """
    last_order = sorted(Order.objects.all(),
                        key=lambda order: order.request_id,
                        reverse=True)[0]
    if last_order.order_status != "New":
        messages.error(request, message="No active orders")
        return redirect('home')
    if request.method == "POST":
        form = AddToOrderForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            order_item = OrderItem.objects.create(
                order=last_order,
                item_name=form.cleaned_data['item_name'],
                unit=form.cleaned_data['unit'],
                quantity=form.cleaned_data['quantity'],
                price_without_vat=form.cleaned_data['price_without_vat']
            )
        return redirect('home')
    else:
        form = AddToOrderForm()
        context = {'form': form}
    return render(request, template_name='warehouse/add_to_last_order.html',
                  context=context)



def decline_request(request):
    """ Declining order (access from coordinator page) """
    id_to_decline = request.GET.get('request_id')
    order = Order.objects.get(request_id=id_to_decline)
    order.order_status = "Declined"
    order.save()
    if request.method == "POST":
        form = DeclinedForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data.get("comment")
            order.comment = comment
            order.save()
            return redirect('coordinator')
    else:
        form = DeclinedForm()
    context = {'form': form}
    return render(request, template_name='warehouse/add_comment_declined.html',
                  context=context)


def accept_request(request):
    """ Accepting order (access from coordinator page) """
    id_to_accept = request.POST.get('request_id')
    order = Order.objects.get(request_id = id_to_accept)
    order_items = OrderItem.objects.filter(order=order)
    correct = True
    for order_item in order_items:
        item = order_item.item_name
        quantity = item.quantity - order_item.quantity
        if item.quantity < order_item.quantity:
            correct = False
            break

    if correct:
        for order_item in order_items:
            item = order_item.item_name
            item.quantity = item.quantity - order_item.quantity
            item.save()
        order.order_status = "Accept"
        order.save()
        return redirect('coordinator')
    else:
        messages.error(request, message="Not enough items")
        return redirect('coordinator')


def open_order(request):
    """ Opening detailed view of items inside the order """
    requested_id = request.GET.get('request_id')
    requested_object = Order.objects.get(request_id = requested_id)
    ordered_items = OrderItem.objects.filter(order = requested_object)
    context = {
        'ordered_items': ordered_items
    }
    return render(request, template_name='warehouse/order_details.html',
                  context=context)