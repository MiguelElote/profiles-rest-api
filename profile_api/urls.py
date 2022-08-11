from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profile_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, 'hello-name')

urlpatterns = [
    path('hello-view', views.HelloAPIView.as_view()),
    path('babysfirst', views.BabysFirstAPIView.as_view()),
    path('', include(router.urls))
    #path('hello-viewset', views.HelloViewSet.as_view({'get':'list'}))
]
