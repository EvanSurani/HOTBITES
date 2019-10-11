"""Factory_stock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from user import views
from adminside import view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('home/',views.home, name="home"),
    path('about_us/',views.about_us, name="about_us"),
    path('contact_us/',views.contact_us, name="contact_us"),
    path('registration/',views.registration, name="registration"),
    path('login/',auth_views.LoginView.as_view(template_name = 'Auth/login.html'), name="login"),
    path('profile/',views.profile, name="profile"),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'Auth/logout.html'), name="logout"),
    path('view_user/',views.view_user, name="view_user"),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('base_admin/',views.base_admin, name="base_admin"),
    path('base_user/',views.base_user, name="base_user"),
    path('add_product_cat/',view.add_product_cat, name="add_product_cat"),
    path('createpost/',view.createpost, name="createpost"),
    path('view_product_cat/',view.view_product_cat, name="view_product_cat"),
    path('del_product_cat/',view.del_product_cat, name="del_product_cat"),
    # path('update_cat/<int:id>',view.update_cat.as_view(), name="update_cat"),
    # path('update_cat/done/',view.update_cat_done, name="update_cat_done"),

]


