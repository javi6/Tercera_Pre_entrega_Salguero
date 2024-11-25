from django.urls import path
from App_00 import views


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),

    path('cursos/', views.cursos, name='cursos'),
    path('cursoForm/', views.cursoForm, name='cursoForm'),
    path('cursoForm2/', views.cursoForm2, name='cursoForm2'),

    path('profesores/', views.profesores, name='profesores'),

    path('estudiantes/', views.estudiantes, name='estudiantes'),

    path('entregables/', views.entregables, name='entregables'),

    path('busquedaCamada/', views.busquedaCamada, name='busquedaCamada'),
    path('buscar/', views.buscar),

]
