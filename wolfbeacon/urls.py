from django.conf.urls import url, include

urlpatterns = [
    # API Views
    url(r'^', include('api.urls')),
]
