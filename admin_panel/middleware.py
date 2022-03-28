from django.urls import  resolve
from django.shortcuts import redirect


class AdminAuthCheckMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        app_name = resolve(request.path).app_name

        if app_name == 'admin_panel':
            if not request.user.is_superuser:
                return redirect('index')

        response = self.get_response(request)

        return response
