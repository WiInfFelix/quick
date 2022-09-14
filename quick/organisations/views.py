from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Organisation
from django.views import generic
# Create your views here.


class IndexView(generic.ListView):
    template_name = "organisations/index.html"
    context_object_name =  "latest_organisations_list"

    def get_queryset(self):
        return Organisation.objects.order_by("created_date")[:5]


class DetailView(generic.DetailView):
    model = Organisation
    template = "organisations/detail.html"
