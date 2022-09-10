# Generated by Django 4.1.1 on 2022-09-08 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('forepons1', models.IntegerField(blank=True, max_length=300, null=True)),
                ('forepons2', models.IntegerField(blank=True, max_length=300, null=True)),
                ('forepons3', models.IntegerField(blank=True, max_length=300, null=True)),
                ('vre_repons', models.IntegerField(blank=True, max_length=300, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': ' a Quiz',
                'verbose_name_plural': 'Quiz',
            },
        ),
    ]