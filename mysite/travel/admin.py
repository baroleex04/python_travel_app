from django.contrib import admin
from .models import Dish, Address

# Register your models here.
class AddressInLine(admin.TabularInline):
    model = Address
    extra = 0
class DishAdmin(admin.ModelAdmin):
    list_display=["dish_name", "add_date", "vote_like"]
    list_filter = ["add_date", "dish_name"]
    search_fields = ["dish_name"]
    fieldsets = [
        ("Name", {"fields": ["dish_name"]}),
        ("Code", {"fields": ["embedded_code"]}),
        ("Date information", {"fields": ["add_date"]}),
        (None, {"fields": ["price", "menu_link"]})
    ]
    inlines = [AddressInLine]
    
admin.site.register(Dish, DishAdmin)
admin.site.register(Address)