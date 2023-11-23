# stocks/urls.py
from django.urls import path
from .views import get_stock_data, index

urlpatterns = [
    path('', index, name='index'),
    path('get_stock_data/', get_stock_data, name='get_stock_data'),
]
