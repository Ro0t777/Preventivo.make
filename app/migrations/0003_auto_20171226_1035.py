# Generated by Django 2.0 on 2017-12-26 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171226_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preventivo',
            name='prezzo',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='preventivo',
            name='ripetizione1',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='preventivo',
            name='ripetizione2',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='preventivo',
            name='ripetizione3',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='preventivo',
            name='ripetizione4',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='preventivo',
            name='ripetizione5',
            field=models.IntegerField(default=1),
        ),
    ]
