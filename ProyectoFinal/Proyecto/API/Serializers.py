from rest_framework import serializers
from App.models import empleados, Actividades,RegistroProyecto

class empeladosSerializer(serializers.ModelSerializer):
    class Meta:
        model = empleados
        fields = ('id',
        'name',
        'puesto',
        'carrera',
        'antiguedad')
class ActividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividades
        fields = (
            'encargado',
            'actividadName',
            'type',
            'estado'
        )

class RegistroProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroProyecto
        fields = (
            'NombreProyecto',
            'Cliente',
            'representante',
            'departamento',
            'FechaRegistro',
            'inicia',
            'finaliza',
            'ObjGeneral',
            'descripcion',
            'userRegistro',
            'status'
        )