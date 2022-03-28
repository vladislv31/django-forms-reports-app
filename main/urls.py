from django.urls import path
from .views import index_view, start_form_view, MainLoginView, MainRegisterView, StartFormView

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', index_view, name='index'),
    path('start-form/', StartFormView.as_view(), name='start-form'),
    path('login/', MainLoginView.as_view(), name='login'),
    path('register/', MainRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]
