from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Conference, Category
from django.urls import reverse_lazy
from django import forms
from reservation.models import Reservation
# Create your views here.

class ConferenceList(ListView):
    model = Conference
    template_name = 'conference_list.html'
    context_object_name = 'conferences'
    ordering = ['start_date']

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__titre=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ConferenceDetailView(DetailView):
    model = Conference
    template_name = 'conference_detail.html'
    context_object_name = 'conference'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservations'] = Reservation.objects.filter(conference=self.object)
        return context

class ConferenceCreateView(CreateView):
    model = Conference
    template_name = 'conference_form.html'
    fields = ['title', 'description', 'program', 'capacity', 'category', 'start_date', 'end_date']
    success_url = reverse_lazy('conference_list')

    def get_form(self):
        form = super().get_form()
        form.fields['program'].widget = forms.FileInput(attrs={'type': 'file', 'class': 'form-control'})
        form.fields['start_date'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        form.fields['end_date'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        return form
    

class ConferenceUpdateView(UpdateView):
    model = Conference
    template_name = 'conference_form.html'
    fields = ['title', 'description', 'program', 'capacity', 'category', 'start_date', 'end_date']
    success_url = reverse_lazy('conference_list')

    def get_form(self):
        form = super().get_form()
        form.fields['program'].widget = forms.FileInput(attrs={'type': 'file', 'class': 'form-control'})
        form.fields['start_date'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        form.fields['end_date'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        return form
    
class ConferenceDeleteView(DeleteView):
    model = Conference
    template_name = 'conference_delete.html'
    success_url = reverse_lazy('conference_list')

def home(request):
    return render(request, 'home.html')