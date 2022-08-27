from django.urls import path

from webapp.views import ProductView, ProductCreate, ProductDetailView, ProductDelete, ProductUpdate, IndexReview

app_name = 'webapp'

urlpatterns = [
    path('', ProductView.as_view(), name='product_view'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='product_delete'),
    path('update/<int:pk>/', ProductUpdate.as_view(), name='product_update'),
    path('product/<int:pk>/review', IndexReview.as_view(), name='product_review'),
]
