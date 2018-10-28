from django.shortcuts import render

# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse
from huobi.models import BlogPost
 
def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template('archive.html')
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))

def index(request):
    t = loader.get_template('index.html')
    c = {
        'dashbox':
               {'myincome':'$1234','incomedetail':'1300, 1877, 2500, 2577, 2000, 2100, 3000, 2700, 3631, 2471, 2700, 3631, 2471',
                'Traffic':'2345','Trafficdetail':'1300, 1877, 2500, 2577, 2000, 2100, 3000, 2700, 3631, 2471, 2700, 3631, 2471',
                'orders':'34234','orderdetail':'1300, 1877, 2500, 2577, 2000, 2100, 3000, 2700, 3631, 2471, 2700, 3631, 2471'
          },
         'live':{'serverload':'34%','serverloadhis':'1300, 1877, 2500, 2577, 2000, 2100, 3000, 2700, 3631, 2471, 2700, 3631, 2471',
                 'Diskper':'34%','Diskhis':'1300, 1877, 2500, 2577, 2000, 2100, 3000, 2700, 3631, 2471, 2700, 3631, 2471',
                 'Transfered':'34%','Transferedhis':'1300, 1877, 2500, 2577, 2000, 2100, 3000, 2700, 3631, 2471, 2700, 3631, 2471',
                 'tasks':1223,'Transfered':5468
          }
        }
    return HttpResponse(t.render(c))

def orderAdd(request):
    t = loader.get_template('car_service/order/orderAdd.html')
    return HttpResponse(t.render())

def orderList(request):
    t = loader.get_template('car_service/order/orders.html')
    return HttpResponse(t.render())

def composeOrderList(request):
    t = loader.get_template('car_service/order/composeOrders.html')
    return HttpResponse(t.render())

def composeReturn(request):
    t = loader.get_template('car_service/order/composeReturn.html')
    return HttpResponse(t.render())

def pricingTable(request):
    t = loader.get_template('car_service/member/pricing-table.html')
    return HttpResponse(t.render())

def purchaseCompose(request):
    t = loader.get_template('car_service/purchase/purchaseCompose.html')
    return HttpResponse(t.render())

def purchaseReturn(request):
    t = loader.get_template('car_service/purchase/purchaseCompose.html')
    return HttpResponse(t.render())

def suppliers(request):
    t = loader.get_template('car_service/purchase/suppliers.html')
    return HttpResponse(t.render())

def composeStock(request):
    t = loader.get_template('car_service/stock/composeWarm.html')
    return HttpResponse(t.render())

def stockInOut(request):
    t = loader.get_template('car_service/stock/composeInOut.html')
    return HttpResponse(t.render())

def stockWarning(request):
    t = loader.get_template('car_service/stock/composeWarm.html')
    return HttpResponse(t.render())

def carList(request):
    t = loader.get_template('car_service/car/carInfo.html')
    return HttpResponse(t.render())

def carEvaluate(request):
    t = loader.get_template('car_service/car/evaluate.html')
    return HttpResponse(t.render())

def owerNotify(request):
    t = loader.get_template('car_service/car/notify.html')
    return HttpResponse(t.render())

def appointment(request):
    t = loader.get_template('car_service/car/appointment.html')
    return HttpResponse(t.render())

