# Generated by Django 4.2.2 on 2023-06-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0002_alter_client_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='favorites',
            field=models.ManyToManyField(to='participant.client'),
        ),
    ]
