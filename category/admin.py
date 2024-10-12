from django.contrib import admin
from participant.models import Participant
from category.models import Category
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin) :
    search_fields = ('title',)
