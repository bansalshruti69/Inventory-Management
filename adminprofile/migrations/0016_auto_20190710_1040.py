# Generated by Django 2.2.2 on 2019-07-10 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminprofile', '0015_returnmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='returnmodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='returnmodel',
            name='item_no',
            field=models.CharField(max_length=1000, primary_key=True, serialize=False),
        ),
    ]
