# Generated by Django 4.2.3 on 2023-07-19 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0003_alter_rpgsetting_options_alter_rpgsetting_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='short_description',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
