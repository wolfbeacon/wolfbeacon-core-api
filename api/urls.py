from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api.views import HackathonViewSet, UserViewSet, HackerList, HackerCreate, HackerRUD, \
    EventCreate, EventRUD, EventList, EventHackerAddRemove, RatingViewSet, FileUploadViewSet

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
    url(r'^hackathons/(?P<fk>\d+)/hackers/$', HackerCreate.as_view()),
    url(r'^hackers/(?P<pk>\d+)/$', HackerRUD.as_view()),
    url(r'^hackers/$', HackerList.as_view()),

    # EVENTS
    url(r'^hackathons/(?P<fk>\d+)/events/$', EventCreate.as_view()),
    url(r'^events/(?P<pk>\d+)/$', EventRUD.as_view()),
    url(r'^events/$', EventList.as_view()),

    # ADD HACKERS TO EVENTS
    url(r'^hackathons/(?P<fk2>\d+)/events/(?P<fk>\d+)/hackers/(?P<pk>\d+)/$', EventHackerAddRemove.as_view()),

    url(r'^file-upload/$', FileUploadViewSet.as_view({'post': 'create'})),

    # Router URLs
    url(r'^', include(router.urls)),

]
