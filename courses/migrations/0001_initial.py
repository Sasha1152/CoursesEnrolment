# Generated by Django 3.0 on 2020-02-18 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
                ('code', models.CharField(max_length=6, unique=True)),
                ('students', models.ManyToManyField(blank=True, related_name='courses', to='students.Student')),
            ],
            options={
                'db_table': 'courses',
            },
        ),
    ]
