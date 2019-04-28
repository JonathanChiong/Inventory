from django.http import HttpResponse, HttpResponseForbidden,Http404
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User
# Call current logged in user
from Ticketing.models import *
from Ticketing.forms import *
import datetime
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)

class Ticketing(CreateView):
    form_class = TransactionForm
    model = Transaction
    template_name = 'Ticketing/ticketing.html'

    def form_valid(self, form):
        from Ticketing.models import Ticket
        transac = form.save()
        newticket = Ticket(transac=transac)
        newticket.save()
        return redirect('TicketHome')

    def get_context_data(self,**kwargs):
        context = super(Ticketing,self).get_context_data(**kwargs)
        context['tickets'] = Ticket.objects.all().order_by('-id')
        return context

class TicketDetail(UpdateView):
    form_class= TicketForm
    model = Ticket
    template_name = 'Ticketing/ticket_detail.html'
    context_object_name= 'ticket'
