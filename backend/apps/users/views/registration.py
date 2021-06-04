from django.views.generic import View
from django.shortcuts import render
from ..services import NewUserRegistration
from django.shortcuts import redirect


class RegistrationView(View):
    """
    Регистрация пользователя
    """

    def get(self, request, *args, **kwargs):
        return render(request, "apps/users/registration-form.html", {})

    def post(self, request, *args, **kwargs):
        service_registration = NewUserRegistration()
        result = service_registration.execute(request.POST)
        if result["errors"]:
            return render(
                request,
                "apps/users/registration-form.html",
                {"errors": result["errors"]},
            )
        else:
            return redirect("login")
