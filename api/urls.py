from django.conf.urls import url
from django.contrib import admin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.models.hackathon_model import Hackathon
from api.serializers.hackathon_serializer import HackathonSerializer
from api.views import root_view

urlpatterns = [
    url(r'^$', root_view.RootView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^hackathons/$', ListCreateAPIView.as_view(queryset=Hackathon.objects.all(), serializer_class=HackathonSerializer), name='hackathon-list-and-create'),
    url(r'^hackathons/(?P<pk>[0-9]+)/$', RetrieveUpdateDestroyAPIView.as_view(queryset=Hackathon.objects.all(), serializer_class=HackathonSerializer), name='hackathon-detail')
]
