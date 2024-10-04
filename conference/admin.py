from django.contrib import admin
from .models import Conference
from reservation.models import Reservation

class ReservationInline(admin.TabularInline):  
    model = Reservation
    extra = 1  

@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):

    list_display = ('title', 'category', 'start_date', 'end_date', 'capacity', 'created_at', 'updated_at')
    
    search_fields = ('title',)
    
    list_per_page = 10
    
    ordering = ('start_date',)
    
    fieldsets = (
        ('Description', {'fields': ('title', 'description', 'category')}),
        ('Dates', {'fields': ('start_date', 'end_date')}),
        ('Programme', {'fields': ('program',)}),
        ('Capacité', {'fields': ('capacity',)}),
        ('Informations de création', {'fields': ('created_at', 'updated_at')}),
    )
    
    readonly_fields = ('created_at', 'updated_at')
    
    inlines = [ReservationInline]
    
    list_filter = (
        'category',
        'start_date',
        ('capacity', admin.BooleanFieldListFilter),
        'title',
    )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if qs is not None:
            return qs.distinct()
        return qs
       
