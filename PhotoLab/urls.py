from django.urls import path

from . import views

app_name = "PhotoLab"
urlpatterns = [
    path('', views.printing, name='printing'),
    path('photo-printing/',views.printing, name='printing'),
    path('photo-creation/',views.creation, name='creation'),
    path('about/',views.about, name='about'),
]