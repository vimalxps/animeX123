# Generated by Django 4.2.3 on 2023-07-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='img',
            field=models.ImageField(default='asd', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
