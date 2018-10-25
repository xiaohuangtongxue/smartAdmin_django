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
    c = {'myincome':'$1234','incomedetail':'1300, 1877, 2500, 2577, 2000, 2100, 3000, 2700, 3631, 2471, 2700, 3631, 2471'}
    #return render(request,'index.html')
    return HttpResponse(t.render(c))