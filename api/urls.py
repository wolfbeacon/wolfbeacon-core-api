from django.contrib import admin
from django.conf.urls import url
from api import views
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.models import Hackathon
from api.serializers import HackathonSerializer

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hackathons/$', ListCreateAPIView.as_view(queryset=Hackathon.objects.all(), serializer_class=HackathonSerializer), name='hackathon-list-and-create'),
    url(r'^hackathon/(?P<pk>[0-9]+)/$', RetrieveUpdateDestroyAPIView.as_view(queryset=Hackathon.objects.all(), serializer_class=HackathonSerializer), name='hackathon-detail')
]
