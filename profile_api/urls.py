from django.urls import path
from profile_api import views

urlpatterns = [
    path('hello-view', views.HelloAPIView.as_view()),
    path('babysfirst', views.BabysFirstAPIView.as_view())
]
