# Generated by Django 4.0.1 on 2023-07-05 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('differentiating_factor', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country_name', models.CharField(max_length=100)),
                ('speciality', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('colour', models.CharField(max_length=100)),
                ('country_of_origin', models.CharField(max_length=100)),
                ('mileage', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mycars', to='mycars.build')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mycars', to='mycars.company')),
            ],
        ),
    ]