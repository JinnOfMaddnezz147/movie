# Generated by Django 4.2.5 on 2023-09-26 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='mimg',
            field=models.ImageField(default=1, upload_to='gallery'),
            preserve_default=False,
        ),
    ]
