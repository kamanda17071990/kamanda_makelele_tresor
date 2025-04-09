from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status  
from rest_framework.response import Response
from .models import Etudiant, Cours, Cote
from .serializers import EtudiantSerializer, CoursSerializer, CoteSerializer

@api_view(['GET'])
def etudiants_list_api(request):
    etudiants = Etudiant.objects.all() 
    serializer = EtudiantSerializer(etudiants, many=True) 
    return Response(serializer.data)  

@api_view(['GET'])
def cours_list_api(request):
    cours = Cours.objects.all()  
    serializer = CoursSerializer(cours, many=True)  
    return Response(serializer.data)  

@api_view(['GET'])
def cote_list_api(request):
    cotes = Cote.objects.all()  
    serializer = CoteSerializer(cotes, many=True)  
    return Response(serializer.data)  

from django.shortcuts import render
from .models import Etudiant

def etudiants_list(request):
    etudiants = Etudiant.objects.all()  # Récupère tous les étudiants
    return render(request, 'gestcotes/etudiants_list.html', {'etudiants': etudiants})


@api_view(['POST'])
def etudiants_create_api(request):
    if request.method == 'POST':
        serializer = EtudiantSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

