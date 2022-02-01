# Generated by Django 3.1.4 on 2021-12-26 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0008_auto_20211213_0914'),
        ('postes', '0012_auto_20211213_0914'),
        ('mensagens', '0001_initial'),
        ('usuarios', '0002_remove_perfil_apelido'),
        ('notificacao', '0004_auto_20211223_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificacao',
            name='data_not',
        ),
        migrations.RemoveField(
            model_name='notificacao',
            name='target_ct',
        ),
        migrations.RemoveField(
            model_name='notificacao',
            name='target_id',
        ),
        migrations.AddField(
            model_name='notificacao',
            name='n_coment1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='n_coment1', to='comentarios.comment'),
        ),
        migrations.AddField(
            model_name='notificacao',
            name='n_coment2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='n_coment2', to='comentarios.comment2'),
        ),
        migrations.AddField(
            model_name='notificacao',
            name='n_follow',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='n_follow', to='usuarios.perfil'),
        ),
        migrations.AddField(
            model_name='notificacao',
            name='n_mensagem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='n_mensagem', to='mensagens.mensagem'),
        ),
        migrations.AddField(
            model_name='notificacao',
            name='n_poste',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='n_poste', to='postes.poste'),
        ),
        migrations.AddField(
            model_name='notificacao',
            name='notification_type',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notificacao',
            name='user_has_seen',
            field=models.BooleanField(default=False),
        ),
    ]
