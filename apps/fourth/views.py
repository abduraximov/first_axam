from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from apps.fourth.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User
#
# class RegisterApiView(APIView):
#
#     def post(self, request):
#         serializer = RegistrationSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             account = serializer.save()
#
#             data['response'] = 'Successfully registered a new user.'
#             data['username'] = account.username
#             data['email'] = account.email
#
#             token = RefreshToken.for_user(account)
#             data['token'] = {
#                 'refresh': str(token),
#                 'access': str(token.access_token)
#             }
#         else:
#             data = serializer.errors
#
#         return Response(data)


class RegisterApiView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        user = self.serializer_class.Meta.model
        refresh_token = RefreshToken.for_user(user)

        data = response.data
        data['refresh_token'] = str(refresh_token)
        data['access_token'] = str(refresh_token.access_token)

        return Response(data)
