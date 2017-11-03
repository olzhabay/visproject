# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Node(models.Model):
	name = models.CharField(max_length=200)
	cpu_cores = models.IntegerField()
	cpu_cores_usage = models.IntegerField(default=0)
	ram_amount = models.IntegerField()
	ram_amount_usage = models.IntegerField(default=0)
	disk_write_max = models.IntegerField()
	disk_write_usage = models.IntegerField(default=0)
	disk_read_max = models.IntegerField()
	disk_read_usage = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class Application(models.Model):
	name = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	started = models.BigIntegerField()
	finished = models.BigIntegerField(blank=True, null=True)

	def __str__(self):
		return self.name


class Container(models.Model):
	name = models.CharField(max_length=200)
	type = models.CharField(max_length=200)
	app_id = models.ForeignKey(Node)
	node_id = models.ForeignKey(Application)
	started = models.BigIntegerField()
	finished = models.BigIntegerField(blank=True, null=True)
	vcore_allocated = models.IntegerField()
	ram_allocated = models.IntegerField()

	def __str__(self):
		return self.name

class Metric(models.Model):
	container_id = models.ForeignKey(Container)
	app_id = models.ForeignKey(Application)
	node_id = models.ForeignKey(Node)
	time = models.BigIntegerField()
	cpu_usage = models.IntegerField()
	ram_usage = models.IntegerField()
	disk_read = models.IntegerField()
	disk_write = models.IntegerField()
	hdfs_read = models.IntegerField()
	hdfs_write = models.IntegerField()
