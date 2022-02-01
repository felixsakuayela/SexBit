from django import forms

from . models import Comment, Comment2

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'C_Texto', 'C_Foto', 'C_Video',
        ]

class CommentForm2(forms.ModelForm):

    class Meta:
        model = Comment2
        fields = [
            'C_Texto2', 'C_Foto2', 'C_Video2',
        ]
