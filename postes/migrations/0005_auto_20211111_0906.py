# Generated by Django 3.1.4 on 2021-11-11 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postes', '0004_auto_20211111_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='poste',
            name='Foto1',
            field=models.ImageField(blank=True, upload_to='Foto/'),
        ),
        migrations.AddField(
            model_name='poste',
            name='Video2',
            field=models.FileField(blank=True, upload_to='Video/'),
        ),
        migrations.AlterField(
            model_name='poste',
            name='Foto',
            field=models.ImageField(blank=True, upload_to='Foto/'),
        ),
        migrations.AlterField(
            model_name='poste',
            name='Video',
            field=models.FileField(blank=True, upload_to='Video/'),
        ),
    ]
