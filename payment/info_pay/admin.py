from django.contrib import admin
from .models import Requisit, Application


class RequisitAdmin(admin.ModelAdmin):
    model = Requisit
    list_display = (
        'id', 'type_payment', 'last_name', 'first_name', 'phone', 'limit', 'card_type', 'account_type')
    list_filter = ('type_payment',)


class ApplicationAdmin(admin.ModelAdmin):
    model = Application
    list_display = ('id', 'summ', 'status', 'requisit','time_create', 'time_update')
    list_filter = ('summ', 'status', 'requisit',)


admin.site.register(Requisit, RequisitAdmin)
admin.site.register(Application, ApplicationAdmin)
