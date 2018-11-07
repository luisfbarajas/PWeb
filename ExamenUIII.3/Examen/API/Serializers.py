from rest_framework import serializers
from App.models import empleados, actividades, RegistroProyecto

class empleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = empleados
        fields = ('id','name','puesto','carrera','antiguedad')


class actividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = actividades
        fields = ('id','name','duracion','empleado')


class RegistroProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroProyecto
        fields = ('id','name','lider','inicia','duracion','reuniones','trabaja')