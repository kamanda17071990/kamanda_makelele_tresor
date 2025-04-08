from django.db import models

class Etudiant(models.Model):
    matricule = models.CharField(max_length=10, unique=True)
    noms = models.CharField(max_length=25)
    genre = models.CharField(
        max_length=1,  
        default='M',
        choices=[('M', 'Masculin'), ('F', 'Feminin')],
    )

    def __str__(self):
        return f"{self.matricule} - {self.noms}"  # Affichage personnalisé

    class Meta:
        db_table = "gestcotes_etudiant"
        managed = True


class Cours(models.Model):
    code = models.CharField(max_length=10, unique=True)
    intituler = models.CharField(max_length=25, default='')

    def __str__(self):
        return f"{self.code} - {self.intituler}"  # Affichage personnalisé

    class Meta:
        db_table = "gestcotes_cours"
        managed = True


class Cote(models.Model):
    etudiant = models.ForeignKey('Etudiant', on_delete=models.CASCADE)
    cours = models.ForeignKey('Cours', on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.etudiant.noms} - {self.cours.intituler} : {self.note}"  # Affichage personnalisé

    class Meta:
        db_table = "gestcotes_cote"
        managed = True
