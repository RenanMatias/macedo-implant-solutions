from django.urls import path

from .views.client import ClientCreateView, ClientListView
from .views.dashboard import DashboardView
from .views.profile import ProfileChangePasswordView, ProfileView

app_name = 'core'
urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/password/', ProfileChangePasswordView.as_view(), name='password'),
    path('clientes/', ClientListView.as_view(), name='client_list'),
    path('clientes/create/', ClientCreateView.as_view(), name='client_create'),
]
