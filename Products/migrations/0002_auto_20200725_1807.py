# Generated by Django 3.0.3 on 2020-07-25 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='description',
            field=models.TextField(default='                                                  ', max_length=300),
        ),
    ]
