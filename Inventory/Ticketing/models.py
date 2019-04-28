from datetime import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

DEPARTMENT = (
    ('Accounting',('Accounting')),
    ('Laboratory',('Laboratory'))
)
SUPPLIER = (
    ('PC EXPRESS',('PC EXPRESS')),
    ('PCX',('PCX'))
)

C_MOTHERBOARD = (
    ('ASROCK',('ASROCK')),
    ('ASUS',('ASUS')),
    ('BIOSTAR',('BIOSTAR')),
    ('GIGABYTE',('GIGABYTE')),
    ('MSI',('MSI')),
)

C_PROCESSOR = (
    ('AMD',('AMD')),
    ('INTEL',('INTEL')),
)
C_MEMORY = (
    ('BINFUL',('BINFUL')),
    ('KILLSRE',('KILLSRE')),
    ('KINGSPEC',('KINGSPEC')),
    ('KINGSTON',('KINGSTON')),
    ('SAMSUNG',('SAMSUNG')),
)

C_LOC = (
    ('Q.C',('Q.C')),
    ('Manila',('Manila')),
)

BRAND_MB = (
    ('ASROCK',('ASROCK')),
    ('ASUS',('ASUS')),
    ('BIOSTAR',('BIOSTAR')),
    ('GIGABYTE',('GIGABYTE')),
    ('MSI',('MSI')),
)

BRAND_PR = (
    ('AMD',('AMD')),
    ('INTEL',('INTEL')),
)

BRAND_MM = (
    ('BINFUL',('BINFUL')),
    ('KILLSRE',('KILLSRE')),
    ('KINGSPEC',('KINGSPEC')),
    ('KIGSTON',('KIGSTON')),
    ('SAMSUNG',('SAMSUNG')),
)

C_STATUS = (
    ('DAMAGED',('DAMAGED')),
    ('IN USE',('IN USE')),
    ('MISSING',('MISSING')),
    ('TRANSFERRED',('TRANSFERRED')),
)

C_TRANSACTION = (
    ('REPAIR',('REPAIR')),
    ('REPLACE',('REPLACE')),
    ('RETURN',('RETURN')),
    ('TRANSFER',('TRANSFER')),
)

class Transaction(models.Model):
    id_comp = models.CharField(max_length=30,null=True,blank=True)
    nm_dept = models.CharField(max_length=50,choices=DEPARTMENT,null=True,blank=True)
    nm_loc = models.CharField(max_length=50,choices=C_LOC,null=True,blank=True)
    nm_supp = models.CharField(max_length=50,choices=SUPPLIER,null=True,blank=True)
    or_no = models.CharField(max_length=30,null=True,blank=True)
    date_req = models.DateField(null=True,blank=True)
    date_pur = models.DateField(null=True,blank=True)

    mb_brand = models.CharField(max_length=50,choices=BRAND_MB,null=True,blank=True)
    mb_mod = models.CharField(max_length=50,null=True,blank=True)
    mb_specs = models.CharField(max_length=50,null=True,blank=True)
    mb_sr = models.CharField(max_length=50,null=True,blank=True)
    pr_brand = models.CharField(max_length=50,choices=BRAND_PR,null=True,blank=True)
    pr_mod = models.CharField(max_length=50,null=True,blank=True)
    pr_specs = models.CharField(max_length=50,null=True,blank=True)
    pr_sr = models.CharField(max_length=50,null=True,blank=True)
    mm_brand = models.CharField(max_length=50,choices=BRAND_MM,null=True,blank=True)
    mm_mod = models.CharField(max_length=50,null=True,blank=True)
    mm_specs = models.CharField(max_length=50,null=True,blank=True)
    mm_sr = models.CharField(max_length=50,null=True,blank=True)

    def get_absolute_url(self):
        return reverse('TicketHome')

    def __str__(self):
        return self.id_comp

class Ticket(models.Model):
    transac = models.ForeignKey(Transaction,on_delete=models.CASCADE,null=True, blank=True)

    mb_stat = models.CharField(max_length=20,choices=C_STATUS,null=True, blank=True)
    pr_stat = models.CharField(max_length=20,choices=C_STATUS,null=True, blank=True)
    mm_stat = models.CharField(max_length=20,choices=C_STATUS,null=True, blank=True)
    mb_tran = models.CharField(max_length=20,choices=C_TRANSACTION,null=True, blank=True)
    pr_tran = models.CharField(max_length=20,choices=C_TRANSACTION,null=True, blank=True)
    mm_tran = models.CharField(max_length=20,choices=C_TRANSACTION,null=True, blank=True)
    mb_war =  models.DateField(null=True, blank=True)
    pr_war =  models.DateField(null=True, blank=True)
    mm_war =  models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('TicketDetail',kwargs={'pk': self.pk})
