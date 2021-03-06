# Generated by Django 3.1.5 on 2021-01-06 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('wagtailimages', '0022_uploadedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogListingsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('headline', models.CharField(default='Här ser du alla blogginlägg som har gjorts :)', help_text='En titel för sidan - sidan som visar alla blogginlägg.', max_length=150)),
                ('subtitle', models.CharField(blank=True, help_text='En underrubrik för sidan - sidan som visar alla blogginlägg.', max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('author', models.CharField(help_text='Här skriver du in namnet på författaren/författarnas.', max_length=150, null=True)),
                ('description', models.TextField(blank=True, help_text='En frivillig kort beskrivning om vad ditt inlägg handlar om.', max_length=300, null=True)),
                ('published', models.DateTimeField(blank=True, help_text='Här skriver jag inget för jag lägger inte in det i FieldPanel ens', null=True)),
                ('presentation_image', models.ForeignKey(blank=True, help_text='En frivillig presentationsbild för ditt inlägg. Om ingen bild väljs så får inlägget automatiskt en standardbild.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
