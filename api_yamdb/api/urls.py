from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, GenreViewSet, TitleViewSet,
                    APISignup, ApiTokenObtain, UserViewSet)


router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router_v1.register('categories', CategoryViewSet)
router_v1.register('genres', GenreViewSet)
router_v1.register('titles', TitleViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', APISignup.as_view(), name='signup'),
    path('v1/auth/token/', ApiTokenObtain.as_view(), name='token'),
]
