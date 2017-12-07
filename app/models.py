# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Server(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Node(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    cpu_cores = models.IntegerField(blank=True, null=True)
    cpu_cores_usage = models.IntegerField(default=0, blank=True, null=True)
    ram_amount = models.IntegerField(blank=True, null=True)
    ram_amount_usage = models.IntegerField(default=0, blank=True, null=True)
    disk_write_max = models.IntegerField(blank=True, null=True)
    disk_write_usage = models.IntegerField(default=0, blank=True, null=True)
    disk_read_max = models.IntegerField(blank=True, null=True)
    disk_read_usage = models.IntegerField(default=0, blank=True, null=True)
    server_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    started = models.BigIntegerField(blank=True, null=True)
    finished = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Container(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    started = models.BigIntegerField(blank=True, null=True)
    finished = models.BigIntegerField(blank=True, null=True)
    vcore_allocated = models.IntegerField(blank=True, null=True)
    ram_allocated = models.IntegerField(blank=True, null=True)
    server_name = models.CharField(max_length=200, blank=True, null=True)
    node_name = models.CharField(max_length=200, blank=True, null=True)
    app_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Metric(models.Model):
    time = models.BigIntegerField(blank=True, null=True)
    time_span = models.BigIntegerField(blank=True, null=True)
    cpu_usage = models.IntegerField(blank=True, null=True)
    ram_usage = models.IntegerField(blank=True, null=True)
    disk_read = models.IntegerField(blank=True, null=True)
    disk_write = models.IntegerField(blank=True, null=True)
    hdfs_read = models.IntegerField(blank=True, null=True)
    hdfs_write = models.IntegerField(blank=True, null=True)
    server_name = models.CharField(max_length=200, blank=True, null=True)
    node_name = models.CharField(max_length=200, blank=True, null=True)
    container_name = models.CharField(max_length=200, blank=True, null=True)
    app_name = models.CharField(max_length=200, blank=True, null=True)
