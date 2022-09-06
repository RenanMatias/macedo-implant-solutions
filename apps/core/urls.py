from django.urls import path

from .views.client import (ClientCreateView, ClientListViewBase,
                           ClientListViewSearch)
from .views.dashboard import DashboardView
from .views.profile import ProfileChangePasswordView, ProfileView

app_name = 'core'
urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/password/', ProfileChangePasswordView.as_view(), name='password'),
    # Client
    path('clients/', ClientListViewBase.as_view(), name='client_list'),
    path('clients/search/', ClientListViewSearch.as_view(), name='client_search'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
]
