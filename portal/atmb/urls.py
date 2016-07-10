from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^thunderBoltPulse/(?P<site_id>[0-9]+)/$', views.thunderBoltPulse, name='thunderBoltPulse'),
    url(r'^editThunderBoltPulse/(?P<site_id>[0-9]+)/$', views.editThunderBoltPulse, name='editThunderBoltPulse'),
    url(r'^thunderExternalProtect/(?P<site_id>[0-9]+)/$', views.thunderExternalProtect, name='thunderExternalProtect'),
    url(r'^editThunderExternalProtect/(?P<site_id>[0-9]+)/$', views.editThunderExternalProtect, name='editThunderExternalProtect'),
    url(r'^postBasicItem/(?P<site_id>[0-9]+)/$', views.postBasicItem, name='postBasicItem'),
    url(r'^basicItem/(?P<site_id>[0-9]+)/$', views.basicItem, name='basicItem'),
    url(r'^wireShield/(?P<site_id>[0-9]+)/$', views.wireShield, name='wireShield'),
]
