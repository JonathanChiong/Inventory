from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from .models import *
from crispy_forms.helper import FormHelper

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'id_comp','nm_dept','nm_loc','nm_supp',
            'or_no','date_req','date_pur','mb_brand',
            'mb_mod','mb_specs','mb_sr','pr_brand',
            'pr_mod','pr_specs','pr_sr','mm_brand',
            'mm_mod','mm_specs','mm_sr',
        ]
        widgets = {
            'id_comp': forms.TextInput(attrs={
            'class': 'form-control'
            }),
            'nm_dept': forms.Select(attrs={
            'class': 'form-control'
            }),
            'nm_loc': forms.Select(attrs={
            'class': 'form-control'
            }),
            'nm_supp': forms.Select(attrs={
            'class': 'form-control'
            }),
            'or_no': forms.TextInput(attrs={
            'class': 'form-control'
            }),
            'date_req': forms.DateInput(attrs={
            'type': 'date'
            }),
            'date_pur': forms.DateInput(attrs={
            'type': 'date',
            }),
# ------------------------------
            'mb_brand': forms.Select(attrs={
            'class': 'form-control'
            }),
            'mb_mod': forms.TextInput(attrs={
            'class': 'form-control'
            }),
            'mb_specs': forms.TextInput(attrs={
            'class': 'form-control'
            }),
            'mb_sr': forms.TextInput(attrs={
            'class': 'form-control'
            }),
# ------------------------------
            'pr_brand': forms.Select(attrs={
            'class': 'form-control'
            }),
            'pr_mod': forms.TextInput(attrs={
            'class': 'form-control'
            }),
            'pr_specs': forms.TextInput(attrs={
            'class': 'form-control'
            }),
            'pr_sr': forms.TextInput(attrs={
            'class': 'form-control'
            }),
# ------------------------------
            'mm_brand': forms.Select(attrs={
            'class': 'form-control'
            }),
            'mm_mod': forms.TextInput(attrs={
            'class': 'form-control'
            }),
            'mm_specs': forms.TextInput(attrs={
            'class': 'form-control'
            }),
            'mm_sr': forms.TextInput(attrs={
            'class': 'form-control'
            }),
            }


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
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
        widgets = {
            'mb_stat': forms.Select(attrs={
            'class': 'form-control'
            }),
            'mb_tran': forms.Select(attrs={
            'class': 'form-control'
            }),
            'mb_war': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'MM-DD-YY'
            }),
            'pr_stat': forms.Select(attrs={
            'class': 'form-control'
            }),
            'pr_tran': forms.Select(attrs={
            'class': 'form-control'
            }),
            'pr_war': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'MM-DD-YY'
            }),
            'mm_stat': forms.Select(attrs={
            'class': 'form-control'
            }),
            'mm_tran': forms.Select(attrs={
            'class': 'form-control'
            }),
            'mm_war': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'MM-DD-YY'
            }),

            }
