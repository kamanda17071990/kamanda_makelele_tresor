from django.db import models

class Classe(models.Model):
    nom = models.CharField(max_length=100)
    niveau = models.CharField(max_length=50)  # Ex: Licence 1, Master 2

    def __str__(self):
        return f"{self.niveau} - {self.nom}"

class Cours(models.Model):
    nom = models.CharField(max_length=100)
    enseignant = models.CharField(max_length=100)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name="cours")

    def __str__(self):
        return self.nom

class Etudiant(models.Model):
    matricule = models.CharField(max_length=20, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    email = models.EmailField()
    classe = models.ForeignKey(Classe, on_delete=models.SET_NULL, null=True, related_name="etudiants")
    cours = models.ManyToManyField(Cours)

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.matricule})"
