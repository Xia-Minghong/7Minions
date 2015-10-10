"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets, permissions

from .serializers import *
from .views import *
from student.views import StudentViewSet
from tag.views import TagViewSet
from event.views import EventViewSet
from organizer.views import OrganizerViewSet
from feedback.views import FeedbackViewSet

admin.autodiscover()


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'students', StudentViewSet)
router.register(r'tags', TagViewSet)
router.register(r'events', EventViewSet)
router.register(r'organizers', OrganizerViewSet)
router.register(r'feedbacks', FeedbackViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#
#     url(r'^event/', include('event.urls')),
#     url(r'^feedback/', include('feedback.urls')),
#     url(r'^organizer/', include('organizer.urls')),
#     url(r'^registration/', include('registration.urls')),
#     url(r'^student/', include('student.urls')),
#     url(r'^tag/', include('tag.urls')),
# ]
