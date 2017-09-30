from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from api.views import HackathonViewSet, UserViewSet, MemberListAndCreate, MemberRUD, RootView

# Register CRUD Entities with Router
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'hackathons', HackathonViewSet,
                base_name='hackathon')  # Note: Mention base_name due to custom query_set

# Additional URLs
urlpatterns = [

    # Root
    url(r'^$', RootView.as_view()),

    # Router URLs
    url(r'^', include(router.urls)),

    # Admin
    url(r'^admin/', admin.site.urls),

    # ADDITIONAL
    # Member Entity
    url(r'^hackathons/(?P<pk>\d+)/members/(?P<fk>\d+)/$', MemberRUD.as_view()),
    url(r'^hackathons/(?P<pk>\d+)/members/$', MemberListAndCreate.as_view()),
]
