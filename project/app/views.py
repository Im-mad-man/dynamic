from django.shortcuts import render
from . import models
from django.views.generic import (ListView,DetailView ,TemplateView,
                                    View)
from .models import CommercialItem

class ItemListView(ListView):
    # dictionaty school_list for us automatically
    #manually context_object_name='schools'
    model = models.CommercialItem

class ItemDetailView(DetailView):
    model =models.CommercialItem
    template_name='app/item_detail.html'


class IndexView(TemplateView):
    template_name='index.html'
