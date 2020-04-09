from django.urls import path, include

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from .views import Signup, BlogViewSet


router = DefaultRouter()
router.register('blog_api', BlogViewSet, base_name='blog')

urlpatterns = [
    path('', obtain_jwt_token, name='redirect_to_obtain_jwt_token'),
    path('login/', obtain_jwt_token, name='obtain_jwt_token'),
    path('signup/', Signup.as_view(), name='signup'),
    path('', include(router.urls)),
]