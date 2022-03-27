from django.contrib import admin
from django.urls import path
from .views import index_view, MainLoginView, MainRegisterView

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', index_view, name='index'),
    path('login/', MainLoginView.as_view(), name='login'),
    path('register/', MainRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]
