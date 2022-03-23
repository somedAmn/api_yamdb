from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.views import APISignup, ApiTokenObtain, UserViewSet

app_name = 'api'

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', APISignup.as_view(), name='signup'),
    path('v1/auth/token/', ApiTokenObtain.as_view(), name='token'),
]
