from django.contrib import admin
from reservation.models import Reservation
# Register your models here.

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('participant', 'conference', 'reservation_date', 'afficher_statut')

    actions = ['confirmer_reservation', 'annuler_reservation']

    def afficher_statut(self, obj):
        return obj.statut
    
    afficher_statut.short_description = 'statut'
    def confirmer_reservation(self, request, queryset):
        queryset.update(statut='confirmee')
        self.message_user(request, "Les reservations sont confirmé")

    def annuler_reservation(self, request, queryset):
        queryset.update(statut='non confirmee')
        self.message_user(request, "Les reservations sont non confirmé")
    
    confirmer_reservation.short_description = "confirmer les reservations"
    annuler_reservation.short_description = "Annuler les reservation"
