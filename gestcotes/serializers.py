from rest_framework import serializers
from .models import Etudiant, Cours, Cote

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'  

class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = '__all__' 

class CoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cote
        fields = '__all__'  
