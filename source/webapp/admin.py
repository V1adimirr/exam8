from django.contrib import admin

from webapp.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'category']
    list_filter = ['category']
    search_fields = ['product_name', 'category']
    fields = ['image', 'product_name', 'description', 'category']


admin.site.register(Product, ProductAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'product', 'text_review', 'rating', 'active_status']
    list_filter = ['created_at']
    search_fields = ['author']
    readonly_fields = ['created_at', 'updated_at']
    fields = ['author', 'product', 'text_review', 'rating', 'active_status', 'created_at', 'updated_at']


admin.site.register(Review, ReviewAdmin)
