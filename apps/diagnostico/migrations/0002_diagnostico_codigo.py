# Generated by Django 3.1.7 on 2023-07-11 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostico',
            name='codigo',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]