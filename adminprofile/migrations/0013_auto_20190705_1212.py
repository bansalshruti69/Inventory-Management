# Generated by Django 2.2.2 on 2019-07-05 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminprofile', '0012_auto_20190705_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
