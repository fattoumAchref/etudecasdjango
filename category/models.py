from django.db import models
from django.core.validators import RegexValidator

class Category(models.Model):
    titre = models.CharField(
        max_length=100, 
        unique=True,
        validators=[RegexValidator(regex=r'^[a-zA-Z\s]+$', message="Le titre doit contenir seulement des caractères.")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return f"{self.titre}"

