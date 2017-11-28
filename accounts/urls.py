from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views


app_name = 'accounts'
urlpatterns = [
    url(r'^$', views.index2, name='index2'),
    url(r'^new$', views.new, name='new'),
    url(r'^create$', views.create, name='create'),
    url(r'^login$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^first-login$', login, {'template_name': 'accounts/first_login.html'}, name='thankslogin'),
    url(r'logout$', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
]