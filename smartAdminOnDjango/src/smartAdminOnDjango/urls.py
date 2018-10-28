"""smartAdminOnDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import  include, url
from django.contrib import admin
from django.contrib.admindocs.views import BookmarkletsView
admin.autodiscover()
from huobi.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('huobi/', archive),
    path('index/', index),
    path('order/add', orderAdd),
    path('order/list', orderList),
    path('order/composeOrderList', composeOrderList),
    path('order/composeReturn', composeReturn),
    path('member/pricingTable', pricingTable),
    path('purchase/compose', purchaseCompose),
    path('purchase/return', purchaseReturn),
    path('purchase/suppliers', suppliers),
    path('stock/compose', composeStock),
    path('stock/inputOutput', stockInOut),
    path('stock/warning', stockWarning), 
    path('car/list', carList), 
    path('car/evaluate', carEvaluate), 
    path('car/owerNotify', owerNotify),
    path('car/appointment', appointment),
]
