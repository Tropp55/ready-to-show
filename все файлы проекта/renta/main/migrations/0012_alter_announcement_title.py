# Generated by Django 4.1.7 on 2023-04-20 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_announcement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Цена за сутки'),
        ),
    ]
