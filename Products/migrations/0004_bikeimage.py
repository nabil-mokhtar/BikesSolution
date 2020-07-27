# Generated by Django 3.0.3 on 2020-07-27 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_auto_20200725_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
                ('Bike', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Products.Bike')),
            ],
        ),
    ]
