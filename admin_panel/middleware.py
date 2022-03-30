from django.urls import  resolve
from django.shortcuts import redirect
from django.conf import settings


class AdminAuthCheckMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        app_name = resolve(request.path).app_name

        if app_name == 'admin_panel':
            if not request.user.is_superuser:
                return redirect('index')

        if request.user.id == settings.GENERAL_ADMIN_ID:
            request.user.is_general_admin = True
        else:
            request.user.is_general_admin = False

        response = self.get_response(request)

        return response
