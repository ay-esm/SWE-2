from django.urls import path
from repair.views import add_customer_view,add_order_view

app_name ="repair"
urlpatterns = [
    path('', add_order_view, name='AddO'),
    path('ay7aga_da_ajax', add_customer_view, name='AddC')
]
