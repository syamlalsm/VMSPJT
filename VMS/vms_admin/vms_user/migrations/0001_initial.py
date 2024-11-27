# Generated by Django 5.1.2 on 2024-11-05 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='vms_user.building')),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='phase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buildings', to='vms_user.phase'),
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('purpose_of_visit', models.CharField(max_length=50)),
                ('visit_date', models.DateField()),
                ('visit_time', models.TimeField()),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vms_user.building')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vms_user.company')),
                ('phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vms_user.phase')),
            ],
        ),
    ]