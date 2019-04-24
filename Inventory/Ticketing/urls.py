from django.urls import path
from . import views
from .views import *


#
# urlpatterns = [
#     path('', Home.as_view(), name='home'),
# # Employee > Status
#     path('employee/status/list/', EmployeeStat.as_view(),
#     name='employeeStat'),
#     path('employee/status/detail/<int:pk>/', EmployeeStatDetail.as_view(),
#     name='employeeStatDetail'),
#     path('employee/status/delete/<int:pk>/', EmployeeStatDelete.as_view(),
#     name='employeeStatDelete'),
#     path('employee/status/create/', EmployeeStatCreate.as_view(),
#     name='employeeStatusCreate'),
#     path('employee/status/update/<int:pk>/', EmployeeStatUpdate.as_view(),
#     name='employeeStatUpdate'),
# ]
