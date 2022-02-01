from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Foto(models.Model):

    User_foto = models.ForeignKey(User, on_delete=models.CASCADE)

    Titulo_foto = models.CharField(max_length=60, blank=True, null=True)

    Nome_foto = models.CharField(max_length=60, blank=True, null=True)

    File_foto = models.ImageField(upload_to='Foto_de_perfil/', blank=True, default='Foto/default.png')

    f_braco_forca = models.ManyToManyField(User, related_name="f_braco_forca", blank=True)
    f_cara_coracao = models.ManyToManyField(User, related_name="f_cara_coracao", blank=True)
    f_cara_surridente = models.ManyToManyField(User, related_name="f_cara_surridente", blank=True)
    f_cara_dinheiro = models.ManyToManyField(User, related_name="f_cara_dinheiro", blank=True)
    f_cara_triste = models.ManyToManyField(User, related_name="f_cara_triste", blank=True)
    f_nao_gosto = models.ManyToManyField(User, related_name="f_nao_gosto", blank=True)

    f_created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    f_updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.Nome_foto}: {self.Titulo_foto}"
