# Generated by Django 3.1.4 on 2021-12-26 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('notificacao', '0005_auto_20211226_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificacao',
            name='n_coment1',
        ),
        migrations.RemoveField(
            model_name='notificacao',
            name='n_coment2',
        ),
        migrations.RemoveField(
            model_name='notificacao',
            name='n_follow',
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
            name='notification_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notificacao',
            name='notification_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_type', to='contenttypes.contenttype'),
        ),
    ]
