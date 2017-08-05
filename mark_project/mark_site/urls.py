from mark_site import views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

  url(r'^$', views.index.as_view(), name='index'),
  url(r'^services/$', views.services.as_view(), name='services'),
  url(r'^gallery/$', views.gallery.as_view(), name='gallery'),
  url(r'^book/$', views.book.as_view(), name='book'),

  #url(r'^$', views.homepage, name="homepage"),
]
