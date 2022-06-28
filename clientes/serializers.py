from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    """validators"""
    def validate(self, data):
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':"CPF inválido"})
        
        if not validate_nome(data['nome']):
            raise serializers.ValidationError({'nome':"Não inclua numeros nesse campo"}) 
        
        if not validate_rg(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve ter 09 dígitos"})
        
        if not validate_cel(data['celular']):
            raise serializers.ValidationError({'celular':"O celular deve ser 00 00000-0000"})
        
        return data