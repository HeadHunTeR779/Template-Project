from django.conf.urls import url
from . import views   #from basic_app import views


#TEMPLATE TAGGING its GLOBAL
app_name = 'basic_app'    #this is its namespace

urlpatterns = [
    url(r'^other/$', views.other_view, name="other"), #If no $ then it WORKS for all other/sadasd or other/askdnk243
                                                        #but after $ only other/
    url(r'^relative/$', views.relative_view, name="relative"),
]
