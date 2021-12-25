# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from dashboard.models import Order
from solookup.models import Boat
from django.core import serializers

def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = Boat.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)