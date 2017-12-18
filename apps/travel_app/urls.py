from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.travels),
    url(r'^/add$',views.add),
    url(r'^/process_trip$',views.process_trip),
    url(r'^/join_trip/(?P<id>\d+)$',views.join_trip),
    url(r'^/destination/(?P<id>\d+)$',views.destination),
    
        
]
