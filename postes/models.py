from django.db import models
from django.contrib.auth.models import User

from PIL import Image


class Poste(models.Model):

    poste_id = models.AutoField(auto_created=True, primary_key=True)

    User_Poste = models.ForeignKey(User, on_delete=models.CASCADE)

    Texto = models.CharField(max_length=261)

    Foto = models.ImageField(upload_to='Foto/', blank=True, null=True)

    Video = models.FileField(upload_to='Video/', blank=True, null=True)

    p_braco_forca = models.ManyToManyField(User, related_name="p_braco_forca", blank=True)
    p_cara_coracao = models.ManyToManyField(User, related_name="p_cara_coracao", blank=True)
    p_cara_surridente = models.ManyToManyField(User, related_name="p_cara_surridente", blank=True)
    p_cara_dinheiro = models.ManyToManyField(User, related_name="p_cara_dinheiro", blank=True)
    p_cara_triste = models.ManyToManyField(User, related_name="p_cara_triste", blank=True)
    p_nao_gosto = models.ManyToManyField(User, related_name="p_nao_gosto", blank=True)

    v_created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    v_updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):

        return self.Texto
        #User_Poste.username