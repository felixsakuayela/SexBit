# Generated by Django 3.1.4 on 2021-11-22 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postes', '0008_auto_20211111_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poste',
            name='Texto',
            field=models.CharField(default=1, max_length=261),
            preserve_default=False,
        ),
    ]