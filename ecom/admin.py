from django.contrib import admin
from .models import Catagory,Customer,Product,Orders,Feedback
# Register your models here.


class CatagoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Catagory, CatagoryAdmin)

class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Orders, OrderAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    pass
admin.site.register(Feedback, FeedbackAdmin)
# Register your models here.
