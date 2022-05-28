from dataclasses import Field
from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.search import index


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("intro", classname="full")]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by("-first_published_at")
        context["blogpages"] = blogpages
        return context


class QuoteBlock(blocks.StructBlock):
    quote_content = blocks.CharBlock()
    person = blocks.CharBlock()
    random_id = blocks.IntegerBlock(required=False)


class SomeStructBlock(blocks.StructBlock):
    random_content = blocks.CharBlock()
    random_date = blocks.DateBlock(required=False)


class BlogPage(Page):
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    content = StreamField(
        [
            ("field1", blocks.CharBlock()),
            ("quote", QuoteBlock()),
            ("date", blocks.DateTimeBlock()),
            ("someblock", SomeStructBlock()),
        ]
    )

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body", classname="full"),
        FieldPanel("content"),
    ]
