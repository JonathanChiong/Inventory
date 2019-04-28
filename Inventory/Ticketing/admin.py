from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.

class RTransaction(resources.ModelResource):
    class Meta:
        model = Transaction
        exclude = ('id')

class ATransaction(ImportExportModelAdmin):
    resources_class = RTransaction
    ordering = ['id_comp']
    list_per_page = 100
    list_display = [
        'id_comp',
        'nm_dept',
        'nm_loc',
        'nm_supp',
        'or_no',
        'date_req',
        'date_pur',
    ]

class RTicket(resources.ModelResource):
    class Meta:
        model = Ticket
        exclude = ('id')

class ATicket(ImportExportModelAdmin):
    resources_class = RTransaction
    ordering = ['id']
    list_per_page = 100
    list_display = [
                'transac',
                'mb_stat',
                'pr_stat',
                'mm_stat',
                'mb_tran',
                'pr_tran',
                'mm_tran',
                'mb_war',
                'pr_war',
                'mm_war',
    ]

admin.site.register(Transaction,ATransaction)
admin.site.register(Ticket,ATicket)
