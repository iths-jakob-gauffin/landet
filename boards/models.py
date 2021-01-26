from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
import datetime

# Create your models here.

class BoardListingsPage(Page):
    parent_page_types = ["home.HomePage"]
    subpage_types = ["boards.BoardPage"]
    max_count = 1
    template = "boards/board_listings_page.html"

    headline = models.CharField(
      max_length=150,
      help_text="Titeln på Anslagstavlan-sidan, förmodligen 'Anslagstavla'",
      blank=False,
      null=False,
      default="Anslagstavlan"
    )

    page_image = models.ForeignKey(
        'wagtailimages.Image',
        related_name="+",
        null=True,
        blank=True,
        help_text="En frivillig bakgrundsbild för sidan.",
        on_delete=models.SET_NULL
    )

    content_panels = Page.content_panels + [
      FieldPanel("headline"),
      ImageChooserPanel("page_image")
    ]

    def get_context(self, request, *args, **kwargs):
      context = super().get_context(request, *args, **kwargs)
      context['boards'] = BoardPage.objects.live().public().order_by('-published')
      return context

class BoardPage(Page):
    parent_page_types = ['boards.BoardListingsPage']
    subpage_types = []
    template = "boards/board_page.html"

    # author = models.CharField(
    #   max_length=150,
    #   default = get_user_model().objects.get('username'),
    #   blank = False,
    #   null = False
    # )
    # auth_user_model = get_user_model()
    # print("HÄR ÄR USERN: ", auth_user_model)
    # default_user = auth_user_model.objects.all()
    # print(default_user)

    # def __init__(self, request, *args, **kwargs):
    #   print(request)

    # author = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.PROTECT
    # )

    page_image = models.ForeignKey(
        'wagtailimages.Image',
        related_name="+",
        null=True,
        blank=True,
        help_text="En frivillig bakgrundsbild för ditt inlägg på anslagstavlan.",
        on_delete=models.SET_NULL
    )

    published = models.DateField(
        blank=True,
        null=False,
        help_text="Här skriver jag inget för jag lägger inte in det i FieldPanel ens",
        default=datetime.date.today
    )

    description = models.TextField(
        max_length=300,
        blank=True,
        null=True,
        help_text="En frivillig kort beskrivning om vad ditt inlägg handlar om."
    )

    content_panels = Page.content_panels + [      
      ImageChooserPanel("page_image"),
      FieldPanel("description")
    ]

