from django.conf.urls import url, include
from django.contrib import admin
from api.views.hackathon_view import HackathonViewSet
from api.views.user_view import UserViewSet
from api.views.member_view import MemberListAndCreate, MemberRUD
from rest_framework.routers import DefaultRouter

# Register CRUD Entities with Router
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'hackathons', HackathonViewSet,
                base_name='hackathon')  # Note: Mention base_name due to custom query_set

# Additional URLs
urlpatterns = [

    url(r'^', include(router.urls)),

    # Hackathons
    url(r'^hackathons/(?P<pk>\d+)/members/(?P<fk>\d+)/$', MemberRUD.as_view()),
    url(r'^hackathons/(?P<pk>\d+)/members/$', MemberListAndCreate.as_view()),

    # Admin
    url(r'^admin/', admin.site.urls),

]
