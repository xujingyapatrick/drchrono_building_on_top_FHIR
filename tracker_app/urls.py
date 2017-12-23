from django.conf.urls import include, url
from django.views.generic import TemplateView

import views
app_name = 'tracker_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/(?P<id>[0-9]+)/$', views.trackingCreate.as_view(), name='tracking-create'),
]