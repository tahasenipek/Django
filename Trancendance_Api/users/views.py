from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    # İsteği doğrulayın.
    if not username or not email or not password:
        return Response({'error': 'Lütfen tüm alanları doldurun.'}, status=status.HTTP_400_BAD_REQUEST)

    # Kullanıcıyı veritabanına kaydedin.
    user = User.objects.create(
        username=username,
        email=email,
        password= make_password(password)
    )

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    # Token'ı kullanıcıya geri döndürün.
    return Response({'success': True, 'access_token': access_token}, status=status.HTTP_201_CREATED)



@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    is_correct = check_password(password, make_password(password))

    if not username or not password:
        return Response({'error': 'Lütfen tüm alanları doldurun.'}, status=status.HTTP_400_BAD_REQUEST)
    
    if not is_correct:
        return Response({'error': 'Kullanıcı adı veya şifre yanlış.'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.get(username=username)
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    return Response({'success': True, 'access_token': access_token}, status=status.HTTP_200_OK)
