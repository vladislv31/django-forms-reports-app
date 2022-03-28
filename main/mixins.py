from django.shortcuts import redirect

from .models import UserOrganizationInfo


class LoginRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        return super().dispatch(request, *args, **kwargs)


class StartFormRequired:

    def dispatch(self, request, *args, **kwargs):
        if not UserOrganizationInfo.objects.filter(user=request.user).exists():
            return redirect('start-form')

        return super().dispatch(request, *args, **kwargs)
