from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')


    if User.objects.filter(username=username).exists():
        return JsonResponse({'error': 'Bu kullanıcı adı zaten kullanımda'}, status=400)
    if not username or not email or not password:
        return Response({'error': 'Lütfen tüm alanları doldurun.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create(
        username=username,
        email=email,
        password= make_password(password),
        is_online=True
    )

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    return Response({'success': True, 'access_token': access_token}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def get_users(request):
    user = request.user
    if not user:
        return Response({'error': 'Lütfen giriş yapın.'}, status=status.HTTP_400_BAD_REQUEST)
    
    users = User.objects.all()
    
    user_data = [ {'username': user.username, 'email': user.email, 'online': user.is_online} for user in users]

    return Response({'success': True, 'user_data': user_data}, status=status.HTTP_200_OK)



@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    is_correct = check_password(password, make_password(password))

    if not username or not password:
        return Response({'error': 'Lütfen tüm alanları doldurun.'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)

    if not user:
        return Response({'error': 'Kullanıcı adı veya şifre yanlış.'}, status=status.HTTP_400_BAD_REQUEST)
    
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    return Response({'success': True, 'access_token': access_token}, status=status.HTTP_200_OK)

