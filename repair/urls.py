from django.urls import path
from repair import views


urlpatterns = [
    path('', views.index)
]
