
from django.contrib import admin
from django.urls import path
from django.conf.urls import  include, url
from django.contrib import admin
admin.autodiscover()
from huobi.views import *


urlpatterns = [
    path('index/', index),
    path('order/add', orderAdd),
    path('order/list', orderList),
    path('order/composeOrderList', composeOrderList),
    path('order/composeReturn', composeReturn),
    path('/member/pricingTable', pricingTable),
    
]
