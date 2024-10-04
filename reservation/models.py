from django.db import models
from participant.models import Participant
from conference.models import Conference
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
class Reservation(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('participant', 'conference')
    
    def clean(self):
        super().clean()
        if self.conference.start_date <= timezone.now():
            raise ValidationError("La réservation ne peut être faite que pour des conférences à venir.")