from django.urls import path

from .views import EventDataAPIView
urlpatterns = [
    path("event_statistic/", EventDataAPIView.as_view())
]