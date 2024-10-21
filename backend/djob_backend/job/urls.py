from django.urls import path

from .views import NewestJobsView

urlpatterns = [
    path('newest/', NewestJobsView.as_view(),),
]
