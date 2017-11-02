from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutView.as_view()),
    url(r'^get_nodes_data/$', views.get_nodes_data, name='get_nodes_data')
]
