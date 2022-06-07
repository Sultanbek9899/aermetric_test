from django.urls import path

from .views import EventDataAPIView
urlpatterns = [
    path("aircraft/event/data/", EventDataAPIView.as_view())
]