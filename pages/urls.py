from django.urls import path
from .views import homeView

app_name='pages'
urlpatterns = [
    path('', homeView, name='Home')
]
