# Generated by Django 2.2.1 on 2019-06-03 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=80, verbose_name='FirstName')),
                ('lastName', models.CharField(max_length=80, verbose_name='LastName')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('cellphone', models.CharField(max_length=200, verbose_name='Cellphone')),
                ('birthDate', models.DateField(verbose_name='BirthDate')),
                ('address', models.CharField(max_length=200, verbose_name='address')),
                ('password', models.CharField(max_length=10, verbose_name='password')),
                ('password2', models.CharField(max_length=10, verbose_name='password2')),
                ('bankAccount', models.CharField(max_length=80, verbose_name='bankAccount')),
                ('licensePlate', models.CharField(max_length=80, verbose_name='LicensePlate')),
                ('cargoVolume', models.CharField(max_length=80, verbose_name='CargoVolume')),
                ('brand', models.CharField(max_length=80, verbose_name='Brand')),
                ('color', models.CharField(max_length=80, verbose_name='Color')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('state', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d/')),
            ],
        ),
    ]