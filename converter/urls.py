from django.urls import path
from . import views
urlpatterns = [
    path('converter/', views.list_conversion_props),
    path('base_currency/', views.take_base_currency, name='currency_pair'),
]
