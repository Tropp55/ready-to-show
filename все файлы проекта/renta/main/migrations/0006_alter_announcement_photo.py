# Generated by Django 4.1.7 on 2023-04-14 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_announcement_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos'),
        ),
    ]
