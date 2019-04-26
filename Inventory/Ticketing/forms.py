from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from .models import *
from crispy_forms.helper import FormHelper

DT_PAY = (
    ('011',('011')),
    ('021',('021')),
    ('031',('031')),
    ('041',('041')),
    ('051',('051')),
    ('061',('061')),
    ('071',('071')),
    ('081',('081')),
    ('091',('091')),
    ('101',('101')),
    ('111',('111')),
    ('121',('121')),
    ('13M',('13M')),
)
#
# class compute_payroll(forms.Form):
#     dt_period = forms.ChoiceField(choices=DT_PAY,required=True,label='')
#
#     def clean(self):
#         from Home.models import t_pay
#         cleaned_data = super(compute_payroll, self).clean()
#         dtpay_select = cleaned_data.get('dt_period')
#
#         payroll = t_pay.objects.all().values('dtpay')
#         pay_list = []
#         for i in payroll:
#             pay_list.append(i['dtpay'])
#
#         if dtpay_select in pay_list:
#             raise forms.ValidationError('This payroll is already generated')
#
#         return self.cleaned_data
