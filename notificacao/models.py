from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from usuarios.models import Perfil
from postes.models import Poste
from mensagens.models import Mensagem
from comentarios.models import Comment
from comentarios.models import Comment2
from PIL import Image


class Notificacao(models.Model):


    notification_type = models.ForeignKey(ContentType, blank=True, null=True, related_name='notification_type',
                                          on_delete=models.CASCADE)
    notification_id = models.PositiveIntegerField(blank=True, null=True)
    link_name = models.CharField(max_length=160, blank=True, null=True)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)

    target = GenericForeignKey('notification_type', 'notification_id')

    notificacao_alert = models.CharField(max_length=240, choices=(
        (1, 'assinou-te a ti'),
        (2, 'enviou-te mensagem'),
        (3, 'comentou na tua foto de perfil'),
        (4, 'reagiu na tua foto de perfil'),
        (5, 'reagiu a um comentario na tua foto de perfil'),
        (6, 'respondeu a um comentario na tua foto de perfil'),
        (7, 'reagiu na tua publicação'),
        (8, 'reagiu a um comentario na tua publicação'),
        (9, 'respondeu a um comentario na tua publicação'),
        (10, 'comentou na tua publicação'),
        (11, 'deixou de ser teu assinante')), blank=True, null=True)

    user_has_seen = models.BooleanField(default=False)

    n_created_at2 = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    n_updated_at2 = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        """Unicode representation for a comment model."""
        return self.owner.username
