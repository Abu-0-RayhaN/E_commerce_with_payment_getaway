from django.db import models
from django.shortcuts import render
from django.views.generic import ListView,DeleteView
from django.views.generic.detail import DetailView
from .models import Product,Category
from django.contrib.auth.mixins import LoginRequiredMixin
class Home(ListView):
    model=Product
    template_name='shop/home.html'

class ProductDetail(LoginRequiredMixin,DetailView):
    model=Product
    template_name='shop/product_detail.html'
    
