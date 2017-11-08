from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from api.views import RootView, HackathonViewSet, UserViewSet, HackerListAndCreate, HackerRUD, \
    EventListAndCreate, EventRUD, EventHackerListAndCreate, RatingViewSet

# Register CRUD Entities with Router
router = DefaultRouter()

# USERS
router.register(r'users', UserViewSet)

# HACKATHONS
router.register(r'hackathons', HackathonViewSet,
                base_name='hackathon')  # Note: Mention base_name due to custom query_set

# RATINGS
router.register(r'ratings', RatingViewSet)

# Additional URLs
urlpatterns = [

    # HACKERS
    url(r'^hackathons/(?P<fk>\d+)/hackers/(?P<pk>\d+)/$', HackerRUD.as_view()),
    url(r'^hackathons/(?P<fk>\d+)/hackers/$', HackerListAndCreate.as_view()),

    # EVENTS
    url(r'^hackathons/(?P<fk>\d+)/events/(?P<pk>\d+)/$', EventRUD.as_view()),
    url(r'^hackathons/(?P<fk>\d+)/events/$', EventListAndCreate.as_view()),

    # HACKERS AT EVENTS
    url(r'^hackathons/(?P<fk>\d+)/events/(?P<pk>\d+)/hackers/$', EventHackerListAndCreate.as_view()),

    # Admin
    url(r'^admin/', admin.site.urls),

    # Router URLs
    url(r'^', include(router.urls)),

    # Root
    url(r'^$', RootView.as_view()),

]
