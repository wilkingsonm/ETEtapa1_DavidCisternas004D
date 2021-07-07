from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Colabreg

class ColabForm(forms.ModelForm):

    class Meta: 
        model= Colabreg
        fields = ['rut', 'nombre', 'telefono', 'email', 'pais', 'contraseña']
        labels ={
            'rut': 'Rut', 
            'nombre': 'Nombre', 
            'telefono': 'Telefono',
            'email': 'Email',
            'pais': 'Pais',
            'contraseña': 'Contraseña',
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su rut', 
                    'id': 'rut',
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre',
                }
            ), 
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su Telefono', 
                    'id': 'telefono',
                }
            ), 
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Email', 
                    'id': 'email',
                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su pais de origen', 
                    'id': 'pais',
                }
            ),
            'contraseña': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su contraseña', 
                    'id': 'contraseña',
                }
            )

        }
