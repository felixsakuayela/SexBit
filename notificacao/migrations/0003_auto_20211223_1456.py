# Generated by Django 3.1.4 on 2021-12-23 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('notificacao', '0002_auto_20211215_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificacao',
            name='n_assinar',
        ),
        migrations.RemoveField(
            model_name='notificacao',
            name='n_comentario1',
        ),
        migrations.RemoveField(
            model_name='notificacao',
            name='n_comentario2',
        ),
        migrations.RemoveField(
            model_name='notificacao',
            name='n_mensagem',
        ),
        migrations.RemoveField(
            model_name='notificacao',
            name='n_poste',
        ),
        migrations.AddField(
            model_name='notificacao',
            name='target_ct',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='target_mod', to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='notificacao',
            name='target_id',
            field=models.PositiveIntegerField(blank=True, db_index=True, null=True),
        ),
    ]
