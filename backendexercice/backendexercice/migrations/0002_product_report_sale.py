# Generated by Django 5.1.3 on 2024-12-03 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendexercice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=256)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
                'indexes': [models.Index(fields=['created_at'], name='backendexer_created_20ff6c_idx'), models.Index(fields=['updated_at'], name='backendexer_updated_6219d4_idx')],
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('In progress', 'In Progress'), ('Failed', 'Failed')], max_length=128)),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
                'indexes': [models.Index(fields=['created_at'], name='backendexer_created_9db81f_idx'), models.Index(fields=['updated_at'], name='backendexer_updated_a9bbea_idx')],
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendexercice.product')),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
                'indexes': [models.Index(fields=['created_at'], name='backendexer_created_5cb3c6_idx'), models.Index(fields=['updated_at'], name='backendexer_updated_746ee7_idx')],
            },
        ),
    ]
