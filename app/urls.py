from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'application', views.ApplicationViewSet)
router.register(r'container', views.ContainerViewSet)
router.register(r'metric', views.MetricViewSet)

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutView.as_view()),
    url(r'^get_nodes_stats/$', views.get_nodes_stats, name='get_nodes_stats'),
    url(r'^get_nodes_status/$', views.get_nodes_status, name='get_nodes_status'),
    url(r'^app_view/$', views.AppView.as_view()),
    url(r'^get_all_apps/$', views.get_all_apps, name='get_all_apps'),
    url(r'^get_app_details/$', views.get_app_details, name='get_app_details'),
    url(r'^get_app_containers/$', views.get_app_containers, name='get_app_containers'),
    url(r'^get_container_metrics/$', views.get_container_metrics, name='get_container_metrics'),
    url(r'^', include(router.urls))
]
