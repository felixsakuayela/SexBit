# Generated by Django 3.1.4 on 2021-12-27 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificacao', '0008_notificacao_notificacao_alert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificacao',
            name='notificacao_alert',
            field=models.CharField(blank=True, choices=[(1, 'assinou-te a ti'), (2, 'enviou-te mensagem'), (3, 'comentou na tua foto de perfil'), (4, 'reagiu na tua foto de perfil'), (5, 'reagiu a um comentario na tua foto de perfil'), (6, 'respondeu a um comentario na tua foto de perfil'), (7, 'reagiu na tua publicação'), (8, 'reagiu a um comentario na tua publicação'), (9, 'respondeu a um comentario na tua publicação'), (10, 'comentou na tua publicação'), (11, 'deixou de ser teu assinante')], max_length=240, null=True),
        ),
    ]