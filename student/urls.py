from django.conf.urls import include, url
from student import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^signup/(?P<matric_no>.*)/(?P<name>.*)/', views.signup, name="signup"),
    url(r'^login', views.login, name="login"),
]