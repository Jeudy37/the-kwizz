# Generated by Django 4.1.1 on 2022-09-08 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz_M', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='forepons1',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='forepons2',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='forepons3',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='vre_repons',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]