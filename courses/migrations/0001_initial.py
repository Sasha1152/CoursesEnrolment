# Generated by Django 3.0 on 2020-01-30 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
                ('code', models.CharField(max_length=6, unique=True)),
                ('users', models.ManyToManyField(blank=True, related_name='courses', to='users.UserProfile')),
            ],
            options={
                'db_table': 'courses',
            },
        ),
    ]
