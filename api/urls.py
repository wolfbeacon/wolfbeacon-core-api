from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from api.views import HackathonViewSet, UserViewSet, HackerListAndCreate, HackerRUD, RootView

# Register CRUD Entities with Router
router = DefaultRouter()

# User Entity
router.register(r'users', UserViewSet)

# Hackathon Entity
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

    # Hacker Entity
    url(r'^hackathons/(?P<fk>\d+)/hackers/(?P<pk>\d+)/$', HackerRUD.as_view()),
    url(r'^hackathons/(?P<fk>\d+)/hackers/$', HackerListAndCreate.as_view()),
]
