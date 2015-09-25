from django.conf.urls import patterns, url
from student import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^home', views.home, name='home'),
)