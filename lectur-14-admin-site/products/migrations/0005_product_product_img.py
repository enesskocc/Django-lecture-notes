# Generated by Django 4.1.1 on 2022-09-27 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_category_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.ImageField(blank=True, default='defaults/clarusway.png', null=True, upload_to='product/'),
        ),
    ]
