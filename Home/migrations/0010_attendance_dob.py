# Generated by Django 2.2.5 on 2019-09-15 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='dob',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
