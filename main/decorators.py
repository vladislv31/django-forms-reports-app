from django.shortcuts import redirect
from functools import wraps

from .models import UserOrganizationInfo


def login_required(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return function(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapper


def start_form_required(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if UserOrganizationInfo.objects.filter(user=request.user).exists():
            return function(request, *args, **kwargs)
        else:
            return redirect('start-form')
    return wrapper
