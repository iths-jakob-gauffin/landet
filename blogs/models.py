from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, RichTextField, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
import datetime

from streams import blocks
from wagtail.core import blocks as wagtail_blocks
# Create your models here.

class BlogListingsPage(Page):
    parent_page_types = ["home.HomePage"]
    subpage_types = ["blogs.BlogPage"]
    max_count = 1
    template = "blogs/blog_listings_page.html"

    headline = models.CharField(
        max_length=150, 
        help_text="En titel för sidan - sidan som visar alla blogginlägg.",
        blank=False,
        null=False,
        default="Här ser du alla blogginlägg som har gjorts :)"
    )
    
    subtitle = models.CharField(
        max_length=255,
        help_text="En underrubrik för sidan - sidan som visar alla blogginlägg.",
        blank=True,
        null=True
    )

    page_image = models.ForeignKey(
        'wagtailimages.Image',
        related_name="+",
        null=True,
        blank=True,
        help_text="En frivillig bakgrundsbild för sidan. Om ingen bild väljs så får inlägget automatiskt en standardbild.",
        on_delete=models.SET_NULL
    )
    
    content_panels = Page.content_panels + [
        FieldPanel("headline"),
        FieldPanel("subtitle"),
        ImageChooserPanel('page_image')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['blogs'] = BlogPage.objects.live().public().order_by('-published')
        # print("lite text på också: ", context['blogs'][0].published)
        return context

class BlogPage(Page):
    parent_page_types = ["blogs.BlogListingsPage"]
    subpage_types = []
    template = "blogs/blog_page.html"

    author = models.CharField(
        max_length=150,
        help_text = "Här skriver du in namnet på författaren/författarna.",
        blank=False,
        null=True
    )

    description = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text="En frivillig kort beskrivning om vad ditt inlägg handlar om."
    )

    page_image = models.ForeignKey(
        'wagtailimages.Image',
        related_name="+",
        null=True,
        blank=True,
        help_text="En frivillig bakgrundsbild för sidan. Om ingen bild väljs så får inlägget automatiskt en standardbild.",
        on_delete=models.SET_NULL
    )

    presentation_image = models.ForeignKey(
        'wagtailimages.Image',
        related_name="+",
        null=True,
        blank=True,
        help_text="En frivillig presentationsbild för ditt inlägg. Om ingen bild väljs så får inlägget automatiskt en standardbild.",
        on_delete=models.SET_NULL
    )

    # start_text = models.TextField(
    #     blank=False,
    #     null=True,
    #     help_text="Här kan du skriva ett längre stycke text, som kommer hamna bredvid din presentationsbild. Det här texten är tänkt att vara 'starttexten' på ditt inlägg.",
    # )

    start_text = RichTextField(help_text="Här kan du skriva ett längre stycke text, som kommer hamna bredvid din presentationsbild. Det här texten är tänkt att vara 'starttexten' på ditt inlägg, och bör, för utseendets skull, vara max 6 rader.")

    published = models.DateField(
        blank=True,
        null=False,
        help_text="Här skriver jag inget för jag lägger inte in det i FieldPanel ens",
        default=datetime.date.today
    )

    body = StreamField([
        ("title", blocks.TitleBlock()),
        ("gallery", blocks.GalleryBlock()),
        ("richText", wagtail_blocks.RichTextBlock()),
        ("imageAndText", blocks.ImageAndText())
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("author"),
        FieldPanel("description"),
        ImageChooserPanel("page_image"),
        ImageChooserPanel("presentation_image"),
        FieldPanel("start_text"),
        StreamFieldPanel("body"),
    ]