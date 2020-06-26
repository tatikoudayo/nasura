from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^database$', views.database, name='database'),
	url(r'^delete$', views.delete, name='delete'),
]