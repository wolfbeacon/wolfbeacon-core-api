from django.conf.urls import url, include
from django.contrib import admin
from api.views import RootView

urlpatterns = [
    # Include api urls
    url(r'^v1/', include('api.urls')),

    # Admin
    url(r'^admin/', admin.site.urls),

    # Root
    url(r'^$', RootView.as_view()),
]
