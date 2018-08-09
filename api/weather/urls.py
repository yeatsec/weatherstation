from django.conf.urls import url
from . import views

PREFIX = 'data'

urlpatterns = [
	url(r'$',views.home),
]
