# Generated by Django 3.1.4 on 2021-12-14 22:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comentarios', '0008_auto_20211213_0914'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('postes', '0012_auto_20211213_0914'),
        ('usuarios', '0002_remove_perfil_apelido'),
        ('mensagens', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=256)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('n_assinar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='n_assinar', to='usuarios.perfil')),
                ('n_comentario1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='n_comentario1', to='comentarios.comment')),
                ('n_comentario2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='n_comentario2', to='comentarios.comment2')),
                ('n_mensagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='n_mensagem', to='mensagens.mensagem')),
                ('n_poste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='n_poste', to='postes.poste')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
