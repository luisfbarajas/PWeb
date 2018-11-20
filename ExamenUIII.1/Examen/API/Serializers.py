from rest_framework import serializers
from App.models import Productos, Personal, LineaProduccion,Entrega,Almacen, ordenes


class OrdenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ordenes
        fields = ('id', 'tipo','solicito','estatus','fecha')
        
class ProductosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Productos
        fields = ('id','typeProduc','estatus')

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = ('id','name', 'lastname','puesto','linea')

class LineaProduccionSerializer(serializers.ModelSerializer):
    jefe = PersonalSerializer(read_only = True, many =True)
    calidad = PersonalSerializer(read_only = True, many =True)
    class Meta:
        model = LineaProduccion
        fields = (
            'id',
            'type',
            'Producto',
            'jefe',
            'calidad',
            'estado'
        )

class EntregaSerializer(serializers.ModelSerializer):
    entrega = PersonalSerializer()
    recibe = PersonalSerializer()
    class Meta:
        model = Entrega
        fields = (
            'id',
            'entrega',
            'recibe',
            'fecha'
        )

class AlmacenSerializer(serializers.ModelSerializer):
    entregas = EntregaSerializer(read_only = True)
    class Meta:
        model = Almacen
        fields = (
            'id',
            'PiezaName',
            'cantidad',
            'typeProduc',
            'entregas'
        )