from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User, Alumno, Maestro, Curso, AsignacionCurso, Tarea

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {"write_only": True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class AlumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class MaestrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maestro
        fields = '__all__'

class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class AsignacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionCurso
        fields = '__all__'

class TareasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'