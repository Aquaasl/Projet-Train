from django.db import models

# Create your models here.

class Train(models.Model):
    nom = models.CharField(max_length=100)
    numero = models.CharField(max_length=50)

    def __str__(self):
        return self.nom
    
