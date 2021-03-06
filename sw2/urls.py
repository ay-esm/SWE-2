from django.urls import path, include
"""sw2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from profiles.views import register_view,list_all_accounts_view,profile_view,edit_profile_view,delete_account_view
from repair.views import *
from pages.views import error_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view),
    path('home/',include('pages.urls')),
    path('repair/',include('repair.urls')),
    path('register/', register_view, name="register"),
    path('error/', error_view, name="error-access"),
    path('repair/additem1', add_items),
    path('login/', auth_views.LoginView.as_view(template_name='profileforms/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('listacc/', list_all_accounts_view, name="listacc"),
    path('profile/<str:username>/', profile_view, name="profile"),
    path('profile/<str:username>/edit', edit_profile_view, name="editprofile"),
    path('profile/<str:username>/delete', delete_account_view, name="deleteprofile"),

]