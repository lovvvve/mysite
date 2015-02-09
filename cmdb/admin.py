from django.contrib import admin
from cmdb.models import *

# Register your models here.

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner',)
    search_fields = ('name', 'owner',)


class HostAdmin(admin.ModelAdmin):
    list_display = ('appname',)
    search_fields = ('appname', )


class ServerAdmin(admin.ModelAdmin):
    list_display = ('serial_number')


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name')


class Ip_addressAdmin(admin.ModelAdmin):
    # list_display = ('ip_address')
    actions_on_top = True


class VMAdmin(admin.ModelAdmin):
    list_display = ('vm_ip')


class HypervisorAdmin(admin.ModelAdmin):
    list_display = ('hypervisor_hostname')


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(Server)
admin.site.register(Contacts)
admin.site.register(Ip_address,Ip_addressAdmin)
admin.site.register(Hypervisor)
admin.site.register(VM)
