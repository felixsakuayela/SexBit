from django.contrib.auth.models import User
from django.db import models

from postes.models import Poste


class Comment(models.Model):
    """
    Model that represents a comment.
    """
    comment_id = models.AutoField(primary_key=True)

    poste_id = models.ForeignKey(Poste, related_name='Poste_id', on_delete=models.CASCADE)

    commenter = models.ForeignKey(User, related_name='posted_comments', on_delete=models.CASCADE)

    C_Texto = models.CharField(max_length=261, blank=True, null=True)

    C_Foto = models.ImageField(upload_to='CFoto/', blank=True, null=True)

    C_Video = models.FileField(upload_to='CVideo/', blank=True, null=True)

    c_braco_forca = models.ManyToManyField(User, related_name="c_braco_forca", blank=True)
    c_cara_coracao = models.ManyToManyField(User, related_name="c_cara_coracao", blank=True)
    c_cara_surridente = models.ManyToManyField(User, related_name="c_cara_surridente", blank=True)
    c_cara_dinheiro = models.ManyToManyField(User, related_name="c_cara_dinheiro", blank=True)
    c_cara_triste = models.ManyToManyField(User, related_name="c_cara_triste", blank=True)
    c_nao_gosto = models.ManyToManyField(User, related_name="c_nao_gosto", blank=True)

    active = models.BooleanField(default=True)
    reply = models.ForeignKey(
        "Comment", related_name='comment_reply', null=True, blank=True, on_delete=models.SET_NULL
    )
    c_created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    c_updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ('c_created_at',)

    def __str__(self):
        """Unicode representation for a comment model."""
        return self.commenter.username
    #poste_id.User_Poste.username|commenter.username



class Comment2(models.Model):
    """
    Model that represents a comment.
    """
    comment_id2 = models.AutoField(primary_key=True)

    comment_id = models.ForeignKey(Comment, related_name='Comment_id', on_delete=models.CASCADE)

    commenter2 = models.ForeignKey(User, related_name='posted_comments2', on_delete=models.CASCADE)

    C_Texto2 = models.CharField(max_length=261, blank=True, null=True)

    C_Foto2 = models.ImageField(upload_to='CFoto/', blank=True, null=True)

    C_Video2 = models.FileField(upload_to='CVideo/', blank=True, null=True)

    c_braco_forca2 = models.ManyToManyField(User, related_name="c_braco_forca2", blank=True)
    c_cara_coracao2 = models.ManyToManyField(User, related_name="c_cara_coracao2", blank=True)
    c_cara_surridente2 = models.ManyToManyField(User, related_name="c_cara_surridente2", blank=True)
    c_cara_dinheiro2 = models.ManyToManyField(User, related_name="c_cara_dinheiro2", blank=True)
    c_cara_triste2 = models.ManyToManyField(User, related_name="c_cara_triste2", blank=True)
    c_nao_gosto2 = models.ManyToManyField(User, related_name="c_nao_gosto2", blank=True)

    active2 = models.BooleanField(default=True)
    reply2 = models.ForeignKey(
        "Comment2", related_name='comment_reply2', null=True, blank=True, on_delete=models.SET_NULL
    )
    c_created_at2 = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    c_updated_at2 = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ('c_created_at2',)

    def __str__(self):
        """Unicode representation for a comment model."""
        return self.commenter2.username
    #poste_id.User_Poste.username|commenter2.username

"""    @staticmethod
    def get_comments(subject_slug=None):
       # Returns comments.
        if subject_slug:
            comments = Comment.objects.filter(active=True,
                                              subject__slug__icontains=subject_slug)
        else:
            comments = Comment.objects.filter(active=True)
        return comments"""