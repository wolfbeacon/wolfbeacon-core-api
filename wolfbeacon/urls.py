from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    # Docs
    url(r'^docs/', get_swagger_view(title='Wolfbeacon API Docs')),

    # API Views
    url(r'^', include('api.urls')),
]
