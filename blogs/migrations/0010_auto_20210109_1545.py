# Generated by Django 3.1.5 on 2021-01-09 14:45

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_blogpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text som visas', required=True))])), ('gallery', wagtail.core.blocks.StructBlock([('gallery', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Frivillig bildtext', max_length='100', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Här lägger du in bilden. Den kommer beskäras enligt måtten 400x400px', required=True))])))])), ('richText', wagtail.core.blocks.RichTextBlock()), ('imageAndText', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Bilden som kommer visas vid sidan av texten.')), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=[]))]))], blank=True, null=True),
        ),
    ]