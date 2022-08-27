from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


class ProductView(ListView):
    model = Product
    template_name = 'products/product_view.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    template_name = 'products/detail_product_view.html'
    model = Product
    context_object_name = 'product'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['tab_product'] = self.object.p.order_by()
    #     return context


class ProductCreate(PermissionRequiredMixin, CreateView):
    form_class = ProductForm
    template_name = 'products/product_create.html'
    permission_required = 'webapp.add_product'

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.pk})

class ProductUpdate(PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'products/product_update.html'
    form_class = ProductForm
    context_key = 'product'
    permission_required = 'webapp.change_project'

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.pk})

class ProductDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'products/product_delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('webapp:product_view')
    permission_required = 'webapp.delete_product'
