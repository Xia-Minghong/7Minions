from django.conf.urls import include, url
from student import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^signup', views.signup, name="signup"),
    url(r'^login', views.login, name="login"),
]