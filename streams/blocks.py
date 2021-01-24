from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock

class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        required=True,
        help_text="Text som visas"
    )

    class Meta:
        template="streams/title_block.html"
        icon="edit"
        label="title"
        help_text="Centrerad text som visas på sidan."

class GalleryBlock(blocks.StructBlock):
    gallery = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(
                    max_length="100", 
                    help_text="Frivillig bildtext", 
                    required=False
                )),
                ("image", ImageChooserBlock(
                    required=True, 
                    help_text="Här lägger du in bilden. Den kommer beskäras enligt måtten 400x400px"
                )),
            ]
        )
    )

    class Meta:
        template="streams/gallery_block.html"
        icon="image"
        label="Standard Gallery"

class ImageAndText(blocks.StructBlock):
    image = ImageChooserBlock(
        help_text="Bilden som kommer visas vid sidan av texten."
    )

    image_alignment = blocks.ChoiceBlock(
        choices = (
            ("Left", "Left"),
            ("Right", "Right"),
        ),
        help_text="Välj om du vill ha bilden till vänster och texten till höger, eller tvärtom."
    )

    caption = blocks.CharBlock(
        max_length=255, 
        required=True
    )
    text = blocks.RichTextBlock()

    class Meta:
        template= "streams/image_and_text.html"
        icon="image"
        label="Bild och text"


class MoviesTableBlock(TableBlock):

    class Meta: 
        template="streams/movie_table_block.html",
        icon="table"
        label="Table"
        help_text = "Skapa en tabell med data."