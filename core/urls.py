# from .views import RegisterAPIView, LoginAPIView, UserAPIView, RefreshAPIView, LogoutView
from django.urls import path, include
from rest_framework import routers
# from . import views
from .views import *
from rest_framework_simplejwt.views import *


router = routers.DefaultRouter()
router.register(r'alumnos', AlumnoView, 'Alumnos')
router.register(r'maestros', MaestrosView, 'Maestros')
router.register(r'cursos', CursoView, 'Cursos')
router.register(r'asignaciones', AsignacionesView, 'Asignaciones')
router.register(r'tareas', TareasViews, 'Tareas')

urlpatterns = [
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('user', UserAPIView.as_view()),
    path('users', UsersAPIView.as_view()),
    path('refresh', RefreshAPIView.as_view()),
    path('logout', LogoutView.as_view()),

    path("", include(router.urls)),
]


