from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutView.as_view()),
    url(r'^get_nodes_stats/$', views.get_nodes_stats, name='get_nodes_stats'),
    url(r'^get_nodes_status/$', views.get_nodes_status, name='get_nodes_status'),
    url(r'^app_view/$', views.AppView.as_view()),
    url(r'^get_app_details/$', views.get_app_details, name='get_app_details')
]
