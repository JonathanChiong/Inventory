from django.urls import path
from . import views
from .views import *



urlpatterns = [
    path('', Ticketing.as_view(), name='TicketHome'),
    path('detail/<int:pk>/', TicketDetail.as_view(), name='TicketDetail'),

]
