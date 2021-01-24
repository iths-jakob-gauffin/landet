from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks

from wagtail.core import blocks as wagtail_blocks

class HomePage(Page):

    lead_text = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Den här texten är underrubrik på startsidan"
    )

    button_text = models.CharField(
        max_length=100,
        help_text="Knappens text på startsidan",
        default="Läs mer",
        null=True
    )

    button = models.ForeignKey(
        "wagtailcore.Page",
        help_text = "Vart knappen på startsidan ska länka till",
        blank=True,
        null=True,
        on_delete = models.SET_NULL,
        related_name="+"
    )

    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        help_text = 'Startsidans bild, s.k. "Hero-bilden"',
        blank=True,
        null=True,
        on_delete = models.SET_NULL,
        related_name="+"
    )

    body = StreamField([
        ("title", blocks.TitleBlock()),
        ("gallery", blocks.GalleryBlock()),
        ("richText", wagtail_blocks.RichTextBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
        FieldPanel("button_text"),
        PageChooserPanel('button'),
        ImageChooserPanel("banner_image"),
        StreamFieldPanel("body"),
    ]
