from django.urls import path

from .views import home_view

urlpatterns = [
    # Include the URLs from the project's apps
    path('', home_view),
]
