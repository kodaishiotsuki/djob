from django.urls import path

from .views import NewestJobsView, JobsDetailView

urlpatterns = [
    path('newest/', NewestJobsView.as_view(),),
    path('<int:pk>/', JobsDetailView.as_view(),),
]
