from django.shortcuts import get_object_or_404,render
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.views import generic
from django.shortcuts import get_object_or_404,render


def index(request):
    return render(request,'homepage/index.html')