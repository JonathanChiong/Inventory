# Generated by Django 2.1.7 on 2019-04-29 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticketing', '0005_auto_20190428_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='id_comp',
            field=models.CharField(default=5, max_length=30),
            preserve_default=False,
        ),
    ]