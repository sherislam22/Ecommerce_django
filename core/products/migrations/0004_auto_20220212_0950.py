# Generated by Django 3.0.10 on 2022-02-12 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220209_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(default=1, upload_to='category_image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='products_image',
            field=models.ImageField(default=1, upload_to='images_products'),
            preserve_default=False,
        ),
    ]