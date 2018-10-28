from django.db import models

from django.contrib import admin
import django.utils.timezone as timezone
 
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
 
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','body','timestamp')
    
class Kline(models.Model):
    symbol = models.CharField(max_length=10)
    amount = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    count = models.IntegerField()
    open = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    close = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    low = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    high = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    vol = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    time = models.DateTimeField(auto_now=False, auto_now_add=False,default=timezone.now,)
    
class ticker(models.Model):
    symbol = models.CharField(max_length=10)
    amount = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    count = models.IntegerField()
    open = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    close = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    low = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    high = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    vol = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    time = models.DateTimeField(auto_now=False, auto_now_add=False,default=timezone.now,)
    
 
admin.site.register(BlogPost,BlogPostAdmin)
