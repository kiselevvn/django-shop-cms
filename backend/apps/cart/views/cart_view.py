from django.views.generic import TemplateView


class CartView(TemplateView):
    template_name = "apps/cart/cart-view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total = 0
        for cart_position in self.request.user.products_in_cart.all():
            total = cart_position.product.price * cart_position.count
        context["total"] = total
        return context
