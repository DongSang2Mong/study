# Generated by Django 3.1.5 on 2021-01-08 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0011_auto_20210108_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaryimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
