from django.contrib import admin
from .models import Cafe, Location, WaiterProfile, CustomerProfile, Join, Transaction

# Register your models here.
class CafeAdmin(admin.ModelAdmin):
    list_display = ('title', 'location')
    list_filter = ('title',)
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Cafe, CafeAdmin)
admin.site.register(Location)
admin.site.register(WaiterProfile)
admin.site.register(CustomerProfile)
admin.site.register(Join)
admin.site.register(Transaction)