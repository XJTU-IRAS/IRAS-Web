# Generated by Django 3.2.16 on 2023-07-15 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20230716_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewee',
            name='gender',
            field=models.CharField(blank=True, db_collation='utf8mb3_bin', max_length=4, null=True),
        ),
    ]
