from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import APIException, AuthenticationFailed
from .authentication import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .models import User

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginAPIView(APIView):
    def post(self, request):
        user = User.objects.filter(email=request.data['email']).first()

        if not user:
            raise APIException('Invalid Credentials!')
        if not user.check_password(request.data['password']):
            raise APIException('Invalid credentials!')
        
        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        response = Response()

        response.set_cookie('refreshToken', value=refresh_token, httponly=True)
        response.data = {
            'token': access_token
        }
        return response
    
class UserAPIView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)

            user = User.objects.filter(pk=id).first()

            return Response(UserSerializer(user).data)
        raise AuthenticationFailed('unauthenticated')
    
# class UsersAPIView(APIView):
#     def get(self, request):
#         auth = get_authorization_header(request).split()

#         if auth and len(auth) == 2:
#             token = auth[1].decode('utf-8')
#             id = decode_access_token(token)

#             user = User.objects.all()

#             return Response(UserSerializer(user).data)
#         raise AuthenticationFailed('unauthenticated')
    
class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refreshToken')
        id = decode_refresh_token(refresh_token)
        access_token = create_access_token(id)
        return Response({
            'token': access_token
        })
    
class LogoutView(APIView): 
    def post(self, request):
        response = Response()
        response.delete_cookie(key="refresh_token")
        response.data = {
            'message' : 'success'
        }
        return response
    
class AlumnoView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = AlumnosSerializer
    queryset = Alumno.objects.all()
   
class MaestrosView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = MaestrosSerializer
    queryset = Maestro.objects.all()

class CursoView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = CursosSerializer
    queryset = Curso.objects.all()

class AsignacionesView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = AsignacionesSerializer
    queryset = AsignacionCurso.objects.all()

class TareasViews(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = TareasSerializer
    queryset = Tarea.objects.all()