# Generated by Django 4.1.1 on 2022-09-30 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0001_initial'),
        ('anotacoes', '0003_rename_mensagem_anotacoes_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anotacoes',
            name='fk_grupo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='grupos.grupo'),
        ),
    ]
