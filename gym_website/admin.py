from django.contrib import admin
from .models import ContactUs, FreeTrial
from django.utils.html import format_html

# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    list_display_links = ('name', )

class FreeTrialAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('myphoto', 'name', 'email', 'phone')
    list_display_links = ('name', )

admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(FreeTrial, FreeTrialAdmin)