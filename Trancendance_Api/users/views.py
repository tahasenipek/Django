from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from django.contrib import auth

@api_view(['POST'])
def register_user(request):
    print("GETTING REGISTER REQUEST")
    # Frontend'den gelen isteği alın.
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    # İsteği doğrulayın.
    if not username or not email or not password:
        return Response({'error': 'Lütfen tüm alanları doldurun.'}, status=status.HTTP_400_BAD_REQUEST)

    # Kullanıcıyı veritabanına kaydedin.
    user = CustomUser.objects.create_user(
        username=username,
        email=email,
        password=password,
    )

    # Kullanıcıya bir oturum açın.
    auth.login(request, user)

    # Kullanıcıyı başarıyla kaydettiğinize dair bir yanıt döndürün.
    return Response({'success': True}, status=status.HTTP_201_CREATED)