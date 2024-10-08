from rest_framework import serializers
from .models import Receipe, Ingredients



class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'

class ReceipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipe
        fields = '__all__'


    def to_representation(self, instance):
        data =  super().to_representation(instance)
        data['ingredients'] = IngredientsSerializer(instance.receipe_indredients.all(),many = True).data
        return data