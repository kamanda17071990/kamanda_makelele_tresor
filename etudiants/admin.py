from django.contrib import admin
from .models import Etudiant, Classe, Cours

@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_display = ('nom', 'niveau')
    search_fields = ('nom', 'niveau')

@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ('nom', 'enseignant', 'classe')
    list_filter = ('classe',)

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'prenom', 'nom', 'classe', 'email')
    list_filter = ('classe',)
    search_fields = ('matricule', 'nom', 'prenom')
