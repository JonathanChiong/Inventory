from django.http import HttpResponse, HttpResponseForbidden,Http404
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User
# Call current logged in user
from Ticketing.models import *
from Ticketing.forms import *
import datetime
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)

# """
#     Set restriction based on user based on parameter.
#     from django.contrib.auth.mixins import UserPassesTestMixin
#
# class VIEW_NAME(UserPassesTestMixin,View)
#     def test_func(self):
#         return self.request.user.userprofile.department == 'HR'
#     allow users if test_func return TRUE / create a list of dept if multiple
#     dept can access ALLOWED_USERS = ['HR','TRAINEE']
#
# """
# class Home(LoginRequiredMixin,TemplateView):
#     template_name = 'home/home.html'
#
# #Employee > Status--------------------------------------------------------------
# class EmployeeStat(LoginRequiredMixin,ListView):
#     model = r_empstat
#     context_object_name = 'emp_stat'
#     template_name = 'references/status/list.html'
#
# class EmployeeStatDetail(LoginRequiredMixin,DetailView):
#     model = r_empstat
#     template_name = 'references/status/detail.html'
#
# class EmployeeStatCreate(LoginRequiredMixin,CreateView):
#     model = r_empstat
#     template_name = 'references/status/create.html'
#     fields = ['cd_empstat','nm_empstat']
#
# class EmployeeStatUpdate(LoginRequiredMixin,UpdateView):
#     model = r_empstat
#     template_name = 'references/status/create.html'
#     fields = ['cd_empstat','nm_empstat']
#
# class EmployeeStatDelete(LoginRequiredMixin,DeleteView):
#     model = r_empstat
#     template_name = 'references/status/delete.html'
#     success_url = '/employee/status/list/'
