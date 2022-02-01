from django import forms

from . models import Perfil

class PerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = [ 'Bio',
            'Genero', 'Interesse', 'Data_de_Nascimento',
            'Nacionalidade','Residencia',
        ]
