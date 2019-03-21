from django.urls import path,include

from .views import repair_piece_input

app_name='piece'
urlpatterns=[
    path('create/',repair_piece_input,name='repair-create'),
]