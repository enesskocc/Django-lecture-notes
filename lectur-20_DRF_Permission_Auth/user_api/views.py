from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view


# Create your views here.
class RegisterView(generics.CreateAPIView): ## Createmodelmixin direk kullanamayiz. Cunku generic apininde kullanlmasi lazim, cunku Api oldugunu belirtmemiz gerekiyor ve bu yüzden CreateApiview cekiyoruz.
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # token = Token.objects.create(user=user)
        token = Token.objects.get(user.user)
        data = serializer.data
        data['token'] = token.key ## data dicoranin icine token atiyoruz.
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
    
    
@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        data = {
            'message': 'logout'
        }
        return Response(data)