from django.db import models
from category.models import Category
from django.core.validators import MaxValueValidator
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.core.exceptions import ValidationError


class Conference(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    program = models.FileField(upload_to='programs/',
                               validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'ppt'])])
    capacity = models.IntegerField(validators=[MaxValueValidator(500)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def clean(self):
        super().clean()
        if self.end_date <= self.start_date:
            raise ValidationError("La date de fin doit être supérieure à la date de début.")
    
    def __str__(self):
        return self.title
