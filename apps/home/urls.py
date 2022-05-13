from django.urls import path

from apps.home.views.site import HomeView

urlpatterns = [
    # Include the URLs from the project's apps
    path('', HomeView.as_view(), name='home'),
]
