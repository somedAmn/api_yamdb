from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken

from api.pagination import UserPagination
from api.permissions import IsAdminOrSuperUser
from api.serializers import (SelfEditSerializer, SignUpSerializer,
                             TokenSerializer, UserSerializer)
from api_yamdb.settings import EMAIL_SUBJECT, FROM_EMAIL, WRONG_CODE_MESSAGE
from reviews.models import User

EMAIL_MASSAGE = format('Confirmation code: {code}')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    lookup_field = 'username'
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrSuperUser,)
    pagination_class = UserPagination

    @action(
        methods=['GET', 'PATCH'],
        detail=False,
        url_path='me',
        serializer_class=SelfEditSerializer,
        permission_classes=(permissions.IsAuthenticated,)
    )
    def user_profile(self, request):
        user = request.user
        if request.method == "PATCH":
            serializer = self.get_serializer(
                user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        serializer = self.get_serializer(user)
        return Response(serializer.data)


class APISignup(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = get_object_or_404(
            User,
            username=serializer.validated_data['username']
        )
        confirmation_code = default_token_generator.make_token(user)
        send_mail(
            subject=EMAIL_SUBJECT,
            message=EMAIL_MASSAGE.format(code=confirmation_code),
            from_email=FROM_EMAIL,
            recipient_list=[user.email],
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class ApiTokenObtain(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        user = get_object_or_404(User, username=username)
        if default_token_generator.check_token(
            user, serializer.validated_data['confirmation_code']
        ):
            token = AccessToken.for_user(user)
            return Response({'token': str(token)}, status=status.HTTP_200_OK)
        return Response(
            {WRONG_CODE_MESSAGE},
            status=status.HTTP_400_BAD_REQUEST
        )
