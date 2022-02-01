from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Perfil(models.Model):

    Usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    Bio = models.CharField(max_length=160, blank=True, null=True)

    followers = models.ManyToManyField(User, related_name="followers_profile", blank=True)

    Genero = models.CharField(max_length=13, choices=(
    ('Lésbica', 'Lésbica'), ('Gay', 'Gay'), ('Bisexual', 'Bisexual'), ('Transexual', 'Transexual'), ('Feminino', 'Feminino'),
    ('Masculino', 'Masculino')), blank=True, null=True)

    Interesse = models.CharField(max_length=13, choices=(
    ('Lésbica', 'Lésbica'), ('Gay', 'Gay'), ('Bisexual', 'Bisexual'), ('Transexual', 'Transexual'), ('Feminino', 'Feminino'),
    ('Masculino', 'Masculino')), blank=True, null=True)


    Data_de_Nascimento = models.DateTimeField(blank=True, null=True)

    Nacionalidade = models.CharField(max_length=54, blank=True, null=True)

    Residencia = models.CharField(max_length=54, blank=True, null=True)

    p_created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    p_updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def get_number_of_followers(self):
        if self.followers.count():
            return self.followers.count()
        else:
            return 0

    def get_number_of_following(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0

    def __str__(self):
        return self.Usuario.username
