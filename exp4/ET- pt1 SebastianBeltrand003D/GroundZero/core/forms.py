from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Moneda, Proveedor,Madera


class ProveedorForm(forms.ModelForm):

    class Meta: 
        model= Proveedor
        fields = ['numIdentificacion', 'nomCompleto', 'telefono', 'direccion', 'email','pais','madera','moneda','montoPago']
        labels ={
            'numIdentificacion': '', 
            'nomCompleto': '', 
            'telefono': '', 
            'direccion': '',
            'email': '',
            'pais': '',
            'madera': '',
            'moneda': '',
            'montoPago': '',
        }
        widgets={
            'numIdentificacion': forms.TextInput(
                attrs={
                    'class': 'barra', 
                    'placeholder': 'Ingrese Num Identificador', 
                    'id': 'numIdentificacion'
                }
            ), 
            'nomCompleto': forms.TextInput(
                attrs={
                    'class': 'barra', 
                    'placeholder': 'Ingrese su nombre completo', 
                    'id': 'nombre'
                }
            ), 
            'telefono': forms.TextInput(
                attrs={
                    'class': 'barra', 
                    'placeholder': 'Ingrese telefono', 
                    'id': 'telefono'
                }
            ), 
            'direccion': forms.TextInput(
                attrs={
                    'class': 'barra', 
                    'placeholder': 'Ingrese direccion', 
                    'id': 'direccion'
                }
            ), 
            'email': forms.TextInput(
                attrs={
                    'class': 'barra',
                    'placeholder': 'Ingrese email',
                    'id': 'email',
                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class': 'barra', 
                    'placeholder': 'Ingrese pais', 
                    'id': 'pais'
                }
            ), 
            'madera': forms.Select(
                attrs={
                    'class': 'barra', 
                    'id': 'madera'
                }
            ), 
            'moneda': forms.Select(
                attrs={
                    'class': 'barra', 
                    'id': 'moneda'
                }
            ), 
            'montoPago': forms.TextInput(
                attrs={
                    'class': 'barra', 
                    'placeholder': 'Ingrese monto base', 
                    'id': 'montoPago'
                }
            ), 

        }

 
    
     
