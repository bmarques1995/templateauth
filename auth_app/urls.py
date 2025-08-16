from django.urls import path
from rest_framework.routers import DefaultRouter
from auth_app.views import echo_route
from auth_app.views import register_user

urlpatterns = [
    path(route='echo_route', view=echo_route, name='echo_route'),
    path(route='register_user', view=register_user, name='register_user'),
]