# Generated by Django 2.2.2 on 2019-07-04 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminprofile', '0003_item_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('Name', models.CharField(blank=True, max_length=1000)),
                ('Description', models.TextField(blank=True)),
                ('Type', models.CharField(blank=True, max_length=1000)),
                ('Unique_Id', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('Bond_Id', models.CharField(blank=True, max_length=1000)),
                ('Date_Of_Order', models.DateField(blank=True)),
                ('Vendor', models.CharField(blank=True, max_length=1000)),
                ('Purchase_Price_Per_Item', models.IntegerField(blank=True)),
                ('Delivered_Date', models.DateField(blank=True)),
                ('Condition', models.CharField(blank=True, max_length=1000)),
                ('Quantity', models.IntegerField(blank=True)),
                ('Asset_Value', models.IntegerField(blank=True)),
                ('Model', models.CharField(blank=True, max_length=1000)),
                ('Vendor_No', models.CharField(blank=True, max_length=1000)),
                ('Remarks', models.TextField(blank=True)),
                ('Photograph', models.ImageField(blank=True, upload_to='')),
                ('Date_Of_Upgrade', models.DateField(blank=True)),
                ('In_use', models.BooleanField(blank=True)),
                ('Replacement_Required', models.BooleanField(blank=True)),
                ('Replacement_Completed', models.BooleanField(blank=True)),
                ('To_be_Discarded', models.BooleanField(blank=True)),
                ('Loaned', models.BooleanField(blank=True)),
            ],
            options={
                'db_table': 'items',
            },
        ),
        migrations.RemoveField(
            model_name='item',
            name='id',
        ),
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.AddField(
            model_name='item',
            name='qty',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='item_no',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='item',
            table=None,
        ),
    ]
