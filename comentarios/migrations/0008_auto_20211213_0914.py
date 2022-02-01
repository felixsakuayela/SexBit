# Generated by Django 3.1.4 on 2021-12-13 08:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comentarios', '0007_auto_20211213_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='c_braco_forca',
            field=models.ManyToManyField(blank=True, related_name='c_braco_forca', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='c_cara_coracao',
            field=models.ManyToManyField(blank=True, related_name='c_cara_coracao', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='c_cara_dinheiro',
            field=models.ManyToManyField(blank=True, related_name='c_cara_dinheiro', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='c_cara_surridente',
            field=models.ManyToManyField(blank=True, related_name='c_cara_surridente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='c_cara_triste',
            field=models.ManyToManyField(blank=True, related_name='c_cara_triste', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='c_nao_gosto',
            field=models.ManyToManyField(blank=True, related_name='c_nao_gosto', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment2',
            name='c_braco_forca2',
            field=models.ManyToManyField(blank=True, related_name='c_braco_forca2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment2',
            name='c_cara_coracao2',
            field=models.ManyToManyField(blank=True, related_name='c_cara_coracao2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment2',
            name='c_cara_dinheiro2',
            field=models.ManyToManyField(blank=True, related_name='c_cara_dinheiro2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment2',
            name='c_cara_surridente2',
            field=models.ManyToManyField(blank=True, related_name='c_cara_surridente2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment2',
            name='c_cara_triste2',
            field=models.ManyToManyField(blank=True, related_name='c_cara_triste2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment2',
            name='c_nao_gosto2',
            field=models.ManyToManyField(blank=True, related_name='c_nao_gosto2', to=settings.AUTH_USER_MODEL),
        ),
    ]
