from django.shortcuts import render
from django.views.generic import ListView
from store.models.category import Electronic

class HomeView(ListView):
    queryset = Electronic.objects.order_by('-id')
    template_name = 'store/home.html'
    context_object_name = 'store'