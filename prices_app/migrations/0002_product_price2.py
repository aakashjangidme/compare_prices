# Generated by Django 3.1 on 2020-08-07 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price2',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]