
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class homepage(TemplateView):
    template_name= 'landing/index.html'
    extra_context = {
        'title' : 'Sailor - Index'
    }

class about(TemplateView):
    template_name='landing/about.html'
    extra_context = {
        'title' : 'Sailor - About'
    }