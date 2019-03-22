from django.urls import path
from . import views

app_name='pages'
urlpatterns = [
    path('', views.homeView, name='Home'),
    path('add', views.add_order_view, name='AddO'),
    path('ay7aga_da_ajax', views.add_customer_view, name='AddC')
]
