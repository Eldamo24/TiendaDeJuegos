from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()
    nombre_usuario = forms.CharField()
    contrasenia = forms.CharField()

class JuegoForm(forms.Form):
    nombre_juego = forms.CharField()
    precio = forms.IntegerField()
    sinopsis = forms.CharField()

class ConsolaForm(forms.Form):
     nombre_consola = forms.CharField()
     precio = forms.IntegerField()

