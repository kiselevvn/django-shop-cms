from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


class LoginView(View):
    """
    Вход на сайт
    """

    def get(self, request, *args, **kwargs):
        return render(request, "apps/users/login-form.html", {})

    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("product-list")
        else:
            return render(
                request,
                "apps/users/login-form.html",
                {"erros": "Пользователь с такими данными не зарегестрирован"},
            )
