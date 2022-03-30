from django.http import Http404


class GeneralAdminRequired:

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_general_admin:
            raise Http404()

        return super().dispatch(request, *args, **kwargs)
