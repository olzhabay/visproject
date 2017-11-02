# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import serializers
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, StreamingHttpResponse, JsonResponse
from django.views.generic import TemplateView
from app.models import Node


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class AboutView(TemplateView):
    template_name = "about.html"


def get_nodes_data(request):
    data = Node.objects.all().values('name', 'cpu_cores', 'ram_amount')
    return JsonResponse(list(data), safe=False)
