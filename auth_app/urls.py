from django.urls import path
from rest_framework.routers import DefaultRouter
from auth_app.views import echo_route

urlpatterns = [
    path(route='echo_route', view=echo_route, name='echo_route'),
]