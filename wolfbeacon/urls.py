from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    # API Views
    url(r'^', include('api.urls')),
]
