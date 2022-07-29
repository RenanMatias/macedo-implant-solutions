from django.urls import path

from .views.dashboard import DashboardView
from .views.profile import ProfileView

app_name = 'core'
urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
