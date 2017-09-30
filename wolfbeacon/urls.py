from django.conf.urls import url, include

urlpatterns = [
    # Include api urls
    url(r'^', include('api.urls')),
]
