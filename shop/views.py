from django.shortcuts import render
from shop.models import Good

# Create your views here.

def shop(request):
    return render(request, 'base.html')

def index(request):
    goods = Good.objects.all().order_by('pk')

    return render(request, 'list.html', {'goods': goods})