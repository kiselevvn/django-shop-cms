from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, re_path, include
from django.conf.urls.i18n import i18n_patterns
from .views import CartView

handler404 = "apps.services.views_error_handlers.handler404"
handler500 = "apps.services.views_error_handlers.handler500"

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^ckeditor/", include("ckeditor_uploader.urls")),
    # path("cart/", CartView.as_view(), name="cart"),
    path(
        "privacy/",
        TemplateView.as_view(template_name="service/privacy.html"),
        name="privacy",
    ),
    path(
        "contacts/",
        TemplateView.as_view(template_name="service/contacts.html"),
        name="contacts",
    ),
    path("", include("apps.products.urls")),
    path("cart/", include("apps.cart.urls")),
    path("users/", include("apps.users.urls")),
    path("orders/", include("apps.orders.urls")),
    # path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path(
        "api/v1/",
        include(
            [
                path("products/", include("apps.products.api")),
                path("orders/", include("apps.orders.api")),
                path("cart/", include("apps.cart.api")),
            ]
        ),
    ),
]

urlpatterns = i18n_patterns(
    *urlpatterns,
    prefix_default_language=False,
)


if settings.DEBUG:
    import debug_toolbar

    # pylint: disable=ungrouped-imports
    from django.conf.urls.static import static

    urlpatterns = (
        [
            path("__debug__/", include(debug_toolbar.urls)),
        ]
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + urlpatterns
    )
