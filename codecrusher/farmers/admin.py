from django.contrib import admin
from farmers.models import farmers
from farmers.models import request
from farmers.models import truckers
# Register your models here.
class farmersAdmin(admin.ModelAdmin):
    list_display= ('name', 'address', 'contact', 'email')

class requestAdmin(admin.ModelAdmin):
    list_display= ('trucktype', 'quantity', 'destination', 'products')

class truckersAdmin(admin.ModelAdmin):
    list_display= ('name', 'address', 'contact', 'email','trucktype')
admin.site.register(farmers,farmersAdmin)
admin.site.register(request,requestAdmin)
admin.site.register(truckers,truckersAdmin)


