from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin
import views
#app_name = 'drchrono'

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^$', views.logout_view, name='login'),
    url(r'^tracker_app/', include('tracker_app.urls', namespace = 'tracker_app')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
]
