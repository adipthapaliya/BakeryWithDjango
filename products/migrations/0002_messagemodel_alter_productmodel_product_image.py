# Generated by Django 4.0.6 on 2022-07-12 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phonenumber', models.CharField(max_length=10)),
                ('message', models.TextField(max_length=225)),
            ],
            options={
                'db_table': 'message',
            },
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='product_image',
            field=models.FileField(upload_to='static/image/product'),
        ),
    ]