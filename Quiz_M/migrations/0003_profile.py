# Generated by Django 4.1 on 2022-09-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz_M', '0002_alter_quiz_forepons1_alter_quiz_forepons2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('modpas1', models.CharField(max_length=50)),
                ('modpas2', models.CharField(max_length=50)),
            ],
        ),
    ]
