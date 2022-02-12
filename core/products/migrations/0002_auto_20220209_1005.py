# Generated by Django 3.0.10 on 2022-02-09 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
        ),
        migrations.AlterField(
            model_name='products',
            name='tag',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.Tags'),
        ),
    ]
