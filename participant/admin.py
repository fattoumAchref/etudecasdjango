from django.contrib import admin
from participant.models import Participant

# Register your models here.
@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'cin', 'email', 'participant_catgory')
    search_fields = ('cin',)