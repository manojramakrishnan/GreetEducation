# Generated by Django 3.2.19 on 2023-07-15 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greet', '0002_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=10, null=True)),
                ('date', models.DateField()),
                ('cl', models.CharField(max_length=10)),
                ('present_status', models.CharField(max_length=10)),
            ],
        ),
    ]
