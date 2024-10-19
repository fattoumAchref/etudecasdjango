from django.urls import path
from . import views

urlpatterns = [
    path('', views.ConferenceList.as_view(), name='conference_list'),
    path('conference/create/', views.ConferenceCreateView.as_view(), name='conference_create'),
    path('conference/<int:pk>/', views.ConferenceDetailView.as_view(), name='conference_detail'),
    path('conference/<int:pk>/update/', views.ConferenceUpdateView.as_view(), name='conference_update'),
    path('conference/<int:pk>/delete/', views.ConferenceDeleteView.as_view(), name='conference_delete'),

]