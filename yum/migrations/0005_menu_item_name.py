# Generated by Django 3.1.5 on 2021-01-23 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yum', '0004_delete_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu_item',
            name='name',
            field=models.CharField(max_length=150, null=True, verbose_name='Описание'),
        ),
    ]
