from django.urls import path

from .views import LoginCreate, LoginView

app_name = 'login'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('login/create/', LoginCreate.as_view(), name='create')
]
