from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api.views import HackathonViewSet, UserViewSet, HackerViewSet, EventViewSet, \
    EventHackerAddRemove, RatingViewSet, PassViewSet, OrganizerViewSet, VolunteerViewSet, MentorViewSet, TeamViewSet

# Register CRUD Entities with Router
router = DefaultRouter()
# USERS
router.register(r'users', UserViewSet)

# HACKATHONS
router.register(r'hackathons', HackathonViewSet,
                base_name='hackathon')  # Note: Mention base_name due to custom query_set

# RATINGS
router.register(r'ratings', RatingViewSet)

# Remaining URLs
urlpatterns = [

    # HACKERS
    url(r'^hackathons/(?P<fk>\d+)/hackers/$', HackerViewSet.as_view({'post': 'create'})),
    url(r'^hackers/(?P<pk>\d+)/$', HackerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    url(r'^hackers/$', HackerViewSet.as_view({'get': 'list'})),

    # ORGANIZERS
    url(r'^hackathons/(?P<fk>\d+)/organizers/$', OrganizerViewSet.as_view({'post': 'create'})),
    url(r'^organizers/(?P<pk>\d+)/$', OrganizerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    url(r'^organizers/$', OrganizerViewSet.as_view({'get': 'list'})),

    # VOLUNTEERS
    url(r'^hackathons/(?P<fk>\d+)/volunteers/$', VolunteerViewSet.as_view({'post': 'create'})),
    url(r'^volunteers/(?P<pk>\d+)/$', VolunteerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    url(r'^volunteers/$', VolunteerViewSet.as_view({'get': 'list'})),

    # MENTORS
    url(r'^hackathons/(?P<fk>\d+)/mentors/$', MentorViewSet.as_view({'post': 'create'})),
    url(r'^mentors/(?P<pk>\d+)/$', MentorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    url(r'^mentors/$', MentorViewSet.as_view({'get': 'list'})),

    # TEAMS
    url(r'^hackathons/(?P<fk>\d+)/teams/$', TeamViewSet.as_view({'post': 'create'})),
    url(r'^teams/(?P<pk>\d+)/$', TeamViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    url(r'^teams/$', TeamViewSet.as_view({'get': 'list'})),

    # EVENTS
    url(r'^hackathons/(?P<fk>\d+)/events/$', EventViewSet.as_view({'post': 'create'})),
    url(r'^events/(?P<pk>\d+)/$', EventViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    url(r'^events/$', EventViewSet.as_view({'get': 'list'})),
    # Add Hackers to Events
    url(r'^hackathons/(?P<fk2>\d+)/events/(?P<fk>\d+)/hackers/(?P<pk>\d+)/$', EventHackerAddRemove.as_view()),

    # HACKER PASSES
    url(r'^passes/$', PassViewSet.as_view({'post': 'create', 'get': 'list'})),
    url(r'^passes/(?P<pk>\d+)/$', PassViewSet.as_view({'delete': 'destroy'})),

    # Router URLs
    url(r'^', include(router.urls)),

]
