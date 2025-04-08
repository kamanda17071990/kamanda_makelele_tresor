
from django.contrib import admin
from .models import Etudiant

class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'noms', 'genre')  # Affichage des colonnes
    search_fields = ('matricule', 'noms')  # Champs pour la recherche
    list_filter = ('genre',)  # Filtres dans l'interface admin

# Enregistrer le modèle avec la classe personnalisée
admin.site.register(Etudiant, EtudiantAdmin)

# Register your models here.

from django.contrib import admin
from .models import Cours

class CoursAdmin(admin.ModelAdmin):
    list_display = ('code', 'intituler')
    search_fields = ('code', 'intituler')
    list_filter = ('intituler',)

admin.site.register(Cours, CoursAdmin)

from django.contrib import admin
from .models import Cote

class CoteAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'cours', 'note', 'date')
    search_fields = ('etudiant__noms', 'cours__nom')
    list_filter = ('cours', 'date')

admin.site.register(Cote, CoteAdmin)



