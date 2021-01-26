# Generated by Django 3.1.5 on 2021-01-25 22:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('wagtailimages', '0022_uploadedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('published', models.DateField(blank=True, default=datetime.date.today, help_text='Här skriver jag inget för jag lägger inte in det i FieldPanel ens')),
                ('description', models.TextField(blank=True, help_text='En frivillig kort beskrivning om vad ditt inlägg handlar om.', max_length=300, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('page_image', models.ForeignKey(blank=True, help_text='En frivillig bakgrundsbild för ditt inlägg på anslagstavlan.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BoardListingsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('headline', models.CharField(default='Anslagstavlan', help_text="Titeln på Anslagstavlan-sidan, förmodligen 'Anslagstavla'", max_length=150)),
                ('page_image', models.ForeignKey(blank=True, help_text='En frivillig bakgrundsbild för sidan.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]