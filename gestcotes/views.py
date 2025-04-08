from django.shortcuts import render #
from django.http import HttpResponse # importer httpres
from django.template import loader  #
from .models import Etudiant   # on importe la classe Etudiant pour afficher

def etudiant(request): # CREER UNE VUE
    mesetudiants = Etudiant.objects.all().values() # selectionner tous les etudiants dans bdd
    contexte = {
        'etudiants' : mesetudiants,
    }
    return render(request, 'afetudiant.html', contexte) # elle va retourner un template

# Create your views here.
