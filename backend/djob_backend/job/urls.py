from django.urls import path

from .views import NewestJobsView, JobsDetailView ,CategoriesView ,BrowseJobsView ,MyJobsView, CreateJobView

urlpatterns = [
    path('', BrowseJobsView.as_view(),),
    path('categories/', CategoriesView.as_view(),),
    path('my/', MyJobsView.as_view(),),
    path('create/', CreateJobView.as_view(),),
    path('newest/', NewestJobsView.as_view(),),
    path('<int:pk>/', JobsDetailView.as_view(),),
    path('<int:pk>/delete/', CreateJobView.as_view(),),
    path('<int:pk>/edit/', CreateJobView.as_view(),),
]
