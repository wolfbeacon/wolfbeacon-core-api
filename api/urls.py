from django.conf.urls import url
from django.contrib import admin
from api.views.root_view import RootView
from api.views.hackathon_view import HackathonListAndCreate, HackathonRUD, MemberListAndCreate, MemberRUD
from api.views.user_view import UserCreate, UserDetail


urlpatterns = [

    # Hackathons
    url(r'^hackathons/(?P<pk>\d+)/members/(?P<fk>\w+)/$', MemberRUD.as_view()),
    url(r'^hackathons/(?P<pk>\d+)/members/$', MemberListAndCreate.as_view()),
    url(r'^hackathons/(?P<pk>\d+)/$', HackathonRUD.as_view()),
    url(r'^hackathons/$', HackathonListAndCreate.as_view()),

    # Users
    url(r'^users/(?P<pk>\w+)/$', UserDetail.as_view()),
    url(r'^users/$', UserCreate.as_view()),

    # Admin
    url(r'^admin/', admin.site.urls),

    # Root
    url(r'^$', RootView.as_view()),
]
