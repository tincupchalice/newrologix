# Generated by Django 4.1.3 on 2022-11-23 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopifyApi',
            fields=[
                ('api_id', models.AutoField(primary_key=True, serialize=False)),
                ('environment', models.CharField(default='test', max_length=100)),
                ('base_url', models.CharField(blank=True, max_length=100, null=True)),
                ('access_token', models.CharField(blank=True, max_length=255, null=True)),
                ('key', models.CharField(blank=True, max_length=255, null=True)),
                ('secret_key', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='XymogenApi',
            fields=[
                ('api_id', models.AutoField(primary_key=True, serialize=False)),
                ('environment', models.CharField(default='test', max_length=100)),
                ('base_url', models.CharField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
