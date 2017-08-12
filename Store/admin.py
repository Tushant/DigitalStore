from django.contrib import admin

from .models import Store, Product, StoreCategory, OpeningHours, ProductImage

admin.site.register(Store)
admin.site.register(Product)
admin.site.register(StoreCategory)
admin.site.register(OpeningHours)
admin.site.register(ProductImage)
