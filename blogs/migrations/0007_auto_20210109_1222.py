# Generated by Django 3.1.5 on 2021-01-09 11:22

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20210108_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='start_text',
            field=wagtail.core.fields.RichTextField(default=None, help_text='Helst 6 rader text.'),
            preserve_default=False,
        ),
    ]
