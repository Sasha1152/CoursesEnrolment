# Generated by Django 3.0 on 2019-12-16 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(default='<23668.', max_length=8, unique=True),
        ),
    ]
