from django.urls import path

from .views import NewestJobsView, JobsDetailView ,CategoriesView ,BrowseJobsView ,MyJobsView

urlpatterns = [
    path('', BrowseJobsView.as_view(),),
    path('categories/', CategoriesView.as_view(),),
    path('my/', MyJobsView.as_view(),),
    path('newest/', NewestJobsView.as_view(),),
    path('<int:pk>/', JobsDetailView.as_view(),),
]
