from django.urls import path
from repair.views import *

app_name ="repair"
urlpatterns = [
    path('', add_order_view, name='AddO'),
    path('add/', add_customer_view, name='AddC'),
    path('addItem/', add_items, name='AddI'),
    path('list/', list_repairs, name='listrepairs')
]
