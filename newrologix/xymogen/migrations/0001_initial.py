# Generated by Django 4.1.3 on 2022-11-22 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(default='N/A', max_length=255)),
            ],
            options={
                'unique_together': {('brand_name',)},
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(default='N/A', max_length=255)),
            ],
            options={
                'unique_together': {('category_name',)},
            },
        ),
        migrations.CreateModel(
            name='Flavor',
            fields=[
                ('flavor_id', models.AutoField(primary_key=True, serialize=False)),
                ('flavor_name', models.CharField(default='N/A', max_length=255)),
            ],
            options={
                'unique_together': {('flavor_name',)},
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='Xymogen/')),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='UnitCount',
            fields=[
                ('unit_count_id', models.AutoField(primary_key=True, serialize=False)),
                ('unit_count_name', models.CharField(default='N/A', max_length=255)),
            ],
            options={
                'unique_together': {('unit_count_name',)},
            },
        ),
        migrations.CreateModel(
            name='XymogenProduct',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=255)),
                ('descriptionShort', models.CharField(max_length=255)),
                ('descriptionFull', models.CharField(max_length=1023)),
                ('productImage', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('count', models.CharField(max_length=255)),
                ('weight', models.FloatField()),
                ('unitWeight', models.CharField(max_length=255)),
                ('wholesalePrice', models.FloatField()),
                ('retailPrice', models.FloatField()),
                ('releaseDate', models.CharField(max_length=255)),
                ('drs', models.CharField(blank=True, max_length=255, null=True)),
                ('upc', models.CharField(default='N/A', max_length=255)),
                ('sku', models.CharField(default='N/A', max_length=255)),
                ('warnings', models.CharField(default='N/A', max_length=255)),
                ('supplementFactsHTML', models.CharField(default='N/A', max_length=255)),
                ('disabled', models.IntegerField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='xproduct_brand', to='xymogen.brand')),
                ('flavor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='xproduct_flavor', to='xymogen.flavor')),
                ('unitCount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='xproduct_unitcount', to='xymogen.unitcount')),
            ],
        ),
        migrations.CreateModel(
            name='XProductDefaultDosingMap',
            fields=[
                ('map_id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.CharField(default='Daily', max_length=255)),
                ('qty', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dosingmap_product', to='xymogen.xymogenproduct')),
            ],
        ),
        migrations.CreateModel(
            name='XProductCategoryMap',
            fields=[
                ('map_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productmap_category', to='xymogen.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productmap_product', to='xymogen.xymogenproduct')),
            ],
        ),
    ]
