# Generated by Django 4.2.4 on 2023-09-05 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_doctors'),
    ]

    operations = [
        migrations.AddField(
            model_name='departments',
            name='dep_img',
            field=models.ImageField(default=0, upload_to='doepartments'),
            preserve_default=False,
        ),
    ]
