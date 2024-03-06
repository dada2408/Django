from django.db import models

# Create your models here.

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    niveau = models.CharField(max_length=100)

class Cours(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()

class Absence(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    justifiee = models.BooleanField()