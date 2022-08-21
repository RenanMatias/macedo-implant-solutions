from django.urls import path

from .views.dashboard import DashboardView
from .views.profile import ProfileChangePasswordView, ProfileView

app_name = 'core'
urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/change_pass/<int:pk>/',
         ProfileChangePasswordView.as_view(),
         name='profile_change_pass'
         ),
]
