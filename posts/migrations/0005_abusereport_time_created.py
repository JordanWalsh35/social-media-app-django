# Generated by Django 3.2.16 on 2023-02-04 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_rename_reportofabuse_abusereport'),
    ]

    operations = [
        migrations.AddField(
            model_name='abusereport',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
