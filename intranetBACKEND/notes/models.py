from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Enum pour le type de note
class TypeNote(models.TextChoices):
    IMPORTANT = "IMPORTANT", "Important"
    INFORMATION = "INFO", "Information"
    EVENEMENT = "EVENT", "Évènement"

# Enum pour l'auteur
class Auteur(models.TextChoices):
    DRH = "DRH", "Direction des Ressources Humaines"
    DIT = "DIT", "Direction des Technologies"
    DG = "DG", "Direction Générale"

# Enum pour la catégorie de document
class CategorieDocument(models.TextChoices):
    RAPPORT = "RAPPORT", "Rapport"
    FORMULAIRE = "FORMULAIRE", "Formulaire"
    PRESENTATION = "PRESENTATION", "Présentation"
    AUTRE = "AUTRE", "Autre"

class Note(models.Model):
    titre = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TypeNote.choices, default=TypeNote.INFORMATION)
    contenu = models.TextField()
    auteur = models.CharField(max_length=10, choices=Auteur.choices)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

class Document(models.Model):
    titre = models.CharField(max_length=255)
    categorie = models.CharField(max_length=20, choices=CategorieDocument.choices, default=CategorieDocument.AUTRE)
    description = models.TextField(blank=True, null=True)
    contenuFichier = models.FileField(upload_to="documents/")
    notes = models.ManyToManyField(Note, related_name="documents", blank=True)

    #def __str__(self):
     #   return self.titre

