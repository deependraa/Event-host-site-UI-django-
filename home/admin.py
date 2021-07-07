from django.contrib import admin
from . models import event
# Register your models here.

class eventAdmin(admin.ModelAdmin):
    list_display = ('id','EventName')
    list_display_links=('id','EventName')
admin.site.register(event,eventAdmin)