from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^regist', views.regist, name="regist"),
    url(r'^login', views.login, name='login'),
    url(r'^main', views.main, name='main'),
    url(r'^user', views.user, name='user'),
    url(r'^wel', views.wel, name='wel')
    ]
