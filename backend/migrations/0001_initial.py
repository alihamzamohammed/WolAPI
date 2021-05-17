# Generated by Django 3.2.3 on 2021-05-17 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('broadcast_address', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('mac_address', models.CharField(max_length=16)),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.network')),
            ],
        ),
    ]