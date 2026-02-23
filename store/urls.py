from django.urls import path
from store import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]