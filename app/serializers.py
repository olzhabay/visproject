from rest_framework import serializers
from app.models import Application, Container, Metric

class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ('name', 'started', 'finished')

class ContainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Container
        fields = ('name', 'app_name', 'node_name',
                  'started', 'finished',
                  'vcore_allocated', 'ram_allocated')

class MetricSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Metric
        fields = ('time', 'time_span', 'cpu_usage', 'ram_usage',
                  'disk_read', 'disk_write', 'hdfs_read', 'hdfs_write')