# Generated by Django 3.0.3 on 2020-07-24 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Records', '0003_auto_20200724_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentrecords',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
