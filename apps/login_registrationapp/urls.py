from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^/register_login$',views.register_login),
    url(r'^/logout',views.logout),
    
    
    
]
