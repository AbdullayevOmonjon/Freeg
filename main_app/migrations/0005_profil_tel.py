# Generated by Django 4.2.1 on 2023-05-11 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_maqola_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='tel',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
