"""
URL configuration for TMAW project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from warehouse import views as warehouse_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='warehouse/login.html'),
         name='login'),
    path('', warehouse_views.home, name='home'),
    path('coordinator/', warehouse_views.coordinator, name='coordinator'),
    path('add_order/', warehouse_views.add_order, name='add_order'),
    path('add_to_last_order/', warehouse_views.add_to_last_order,
         name='add_to_last_order'),
    path('add_item/', warehouse_views.add_item, name='add_item'),
    path('delete_item/', warehouse_views.delete_item, name='delete_item'),
    path('modify_item/', warehouse_views.modify_item, name='modify_item'),
    path('decline_request/', warehouse_views.decline_request, name='decline_request'),
    path('accept_request/', warehouse_views.accept_request, name='accept_request'),
    path('delete_order/', warehouse_views.delete_order, name='delete_order'),
    path('open_order/', warehouse_views.open_order, name='open_order')
]
