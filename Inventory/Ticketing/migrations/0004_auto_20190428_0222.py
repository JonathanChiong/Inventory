# Generated by Django 2.1.7 on 2019-04-27 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticketing', '0003_auto_20190428_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='mb_mod',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='mb_specs',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='mb_sr',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='mm_brand',
            field=models.CharField(blank=True, choices=[('BINFUL', 'BINFUL'), ('KILLSRE', 'KILLSRE'), ('KINGSPEC', 'KINGSPEC'), ('KIGSTON', 'KIGSTON'), ('SAMSUNG', 'SAMSUNG')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='mm_mod',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='mm_specs',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='mm_sr',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='pr_brand',
            field=models.CharField(blank=True, choices=[('AMD', 'AMD'), ('INTEL', 'INTEL')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='pr_mod',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='pr_specs',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='pr_sr',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]