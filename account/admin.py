from django.contrib import admin
from .models import User,Shipment,Employee

# Register your models here.
admin.site.register(User)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'statuses',
    )
    readonly_fields  = ('Cost_In_Dollars',)
admin.site.register(Shipment,ShipmentAdmin)
admin.site.register(Employee)