from django.contrib import admin
from Ticketing.models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.

# class t_otResource(resources.ModelResource):
#     class Meta:
#         model = t_ot
#         exclude = ('id')
#
# class t_otAdmin(ImportExportModelAdmin):
#     resources_class = t_otResource
#     ordering = ['dtpay']
#     list_per_page = 100
#     list_display = [
#         'empno',
#         'dtpay',
#         'cd_ot',
#         'ot_hrs',
#         'ot_amt',
#         'ty_ot',
#         'cd_user',
#         'accesstime',
#     ]
#
# admin.site.register(sss_t,SSSAdmin)
