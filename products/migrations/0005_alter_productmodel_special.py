# Generated by Django 4.0.6 on 2022-07-15 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_productmodel_special'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='special',
            field=models.TextField(blank=True, default=None, max_length=10, null=True),
        ),
    ]