from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=20)
    camada = forms.IntegerField()

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=20)