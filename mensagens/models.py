from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Mensagem(models.Model):
    """
    Model that represents a message.
    """
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    caixa = models.TextField(max_length=1000, blank=True)

    m_created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    m_updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    rec_user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)

    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ('m_created_at',)

    def __str__(self):
        """Unicode representation for a message model."""
        return self.caixa