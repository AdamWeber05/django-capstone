from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

def main(request):
    return redirect('/solookup/')
