# Generated by Django 4.1.1 on 2022-09-12 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anotacoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anotacoes',
            name='fk_pessoa',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
