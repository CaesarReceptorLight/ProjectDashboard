# Author: Sheeba Samuel, <sheeba.samuel@uni-jena.de> https://github.com/Sheeba-Samuel

from django.conf.urls import url, patterns
from projectdashboard import views


urlpatterns = patterns('django.views.generic.simple',

    url(r'^getProjectDashboard/$', views.getProjectDashboard, name="getProjectDashboard"),
    url(r'^getServerResponse/'
        r'(?P<project_id>[\w ]+)/(?P<input_type>\w+)/$', views.getServerResponse, name="getServerResponse"),
    url(r'^getPropertyResponse/(?P<input>\w+)/$', views.getPropertyResponse, name="getPropertyResponse"),

    # API
    url(r'^$',
        lambda x: None,
        name='projectdashboard_base'),

)
