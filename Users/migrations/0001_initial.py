# Generated by Django 3.0.7 on 2020-06-30 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('adress', models.CharField(max_length=30)),
                ('idImage', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='RentReservations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDateTime', models.DateTimeField()),
                ('notes', models.TextField(max_length=100)),
                ('duration', models.DurationField()),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.Bike')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.User')),
            ],
        ),
        migrations.CreateModel(
            name='FixReservations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(max_length=100)),
                ('dateTime', models.DateTimeField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.Service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.User')),
            ],
        ),
    ]
