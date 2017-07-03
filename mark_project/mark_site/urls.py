from mark_site import views
from django.conf.urls import url

urlpatterns = [
  url(r'^$', views.index.as_view(), name='index'),
  #url(r'^$', views.homepage, name="homepage"),
]
