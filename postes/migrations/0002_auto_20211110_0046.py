# Generated by Django 3.1.4 on 2021-11-09 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poste',
            name='Foto',
            field=models.ImageField(blank=True, default=1, upload_to='Foto/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='poste',
            name='Video',
            field=models.FileField(blank=True, default=1, upload_to='Video/'),
            preserve_default=False,
        ),
    ]
