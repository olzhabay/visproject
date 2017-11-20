# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

from django.core import serializers
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, StreamingHttpResponse, JsonResponse
from django.template import RequestContext
from django.views.generic import TemplateView
from django import forms
from rest_framework import viewsets
from app.serializers import *

from app.models import Node, Application, Container
import json


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class AboutView(TemplateView):
    template_name = "about.html"


class AppView(TemplateView):
    def get(self, request, **kwargs):
        apps = Application.objects.all().values('name')
        context = { 'applications' : apps, }
        return render(request, 'app_view.html', context=context)


def get_nodes_stats(request):
    data = Node.objects.all().values('name', 'cpu_cores', 'ram_amount')
    return JsonResponse(list(data), safe=False)


def get_nodes_status(request):
    data = Node.objects.all().values('name', 'cpu_cores', 'cpu_cores_usage', 'ram_amount', 'ram_amount_usage')
    return JsonResponse(list(data), safe=False)


def get_app_details(request):
    global app_data
    if request.method == 'POST':
        app_name = request.POST['app_name']
        app_data = Application.objects.get(name=app_name)
    return HttpResponse(content=app_data)


def get_app_containers(request):
    global container_data
    if request.method == 'POST':
        app_name = request.POST['app_name']
        container_data = Container.objects.all().filter(app_name=app_name)
    return JsonResponse(list(container_data), safe=False)


def nodes_status_chart(request):
    name = Node.objects.all().values('name')
    cpu_cores = Node.objects.all().values('cpu_cores')
    cpu_cores_usage = Node.objects.all().values('cpu_cores_usage')
    cpu_percent = cpu_cores_usage / cpu_cores
    ram_amount = Node.objects.all().values('ram_amount')
    ram_amount_usage = Node.objects.all().values('ram_amount_usage')
    ram_percent = ram_amount_usage / ram_amount
    extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
    chartdata = {
        'x': name,
        'name1': "series 1", 'y1': cpu_percent, 'extra1': extra_serie,
        'name2': "series 2", 'y2': ram_percent, 'extra2': extra_serie
    }
    charttype = "multiBarChart"
    data = {
        'charttype': charttype,
        'chartdate': chartdata
    }
    return render_to_response('nodes_status_chart.html', data)


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ContainerViewSet(viewsets.ModelViewSet):
    queryset =  Container.objects.all()
    serializer_class = ContainerSerializer

class MetricViewSet(viewsets.ModelViewSet):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer

