from django.urls import path
from .views import *
urlpatterns = [
  path('',Index_view.as_view(),name='index'),
  path('about/',About_view.as_view(),name='about'),
  path('service/',Service_view.as_view(),name='service'),
  path('contact/',Contact_view.as_view(),name='contact'),
]