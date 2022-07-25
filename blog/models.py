from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from wagtail.models import Page, RevisionMixin
from wagtail.fields import RichTextField, StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet


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


class ImportantDatesBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    description = blocks.CharBlock(required=False)
    date = blocks.DateBlock()


class SomeStreamBlock(blocks.StreamBlock):
    title = blocks.CharBlock()
    content = blocks.CharBlock()


class BlogPage(Page):
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    content = StreamField(
        [
            ("field1", blocks.CharBlock()),
            ("quote", QuoteBlock()),
            ("date", blocks.DateTimeBlock()),
            ("someblock", SomeStructBlock()),
            ("important_dates", ImportantDatesBlock()),
            ("somestreamblock", SomeStreamBlock()),
            ("hpcharacters", blocks.ListBlock(blocks.CharBlock())),
        ],
        blank=True,
        use_json_field=True,
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


@register_snippet
class SampleModel(models.Model):
    name = models.CharField(max_length=255)
    stream_content = StreamField(
        [
            ("field1", blocks.CharBlock()),
            ("quote", QuoteBlock()),
            ("date", blocks.DateTimeBlock()),
            ("someblock", SomeStructBlock()),
            ("important_dates", ImportantDatesBlock()),
            ("somestreamblock", SomeStreamBlock()),
            ("hpcharacters", blocks.ListBlock(blocks.CharBlock())),
        ],
        blank=True,
        use_json_field=True,
    )

@register_snippet
class SampleModelWithRevisions(RevisionMixin, models.Model):
    name = models.CharField(max_length=255)
    stream_content = StreamField(
        [
            ("field1", blocks.CharBlock()),
            ("quote", QuoteBlock()),
            ("date", blocks.DateTimeBlock()),
            ("someblock", SomeStructBlock()),
            ("important_dates", ImportantDatesBlock()),
            ("somestreamblock", SomeStreamBlock()),
            ("hpcharacters", blocks.ListBlock(blocks.CharBlock())),
        ],
        blank=True,
        use_json_field=True,
    )
    _revisions = GenericRelation("wagtailcore.Revision", related_query_name="samplerevision")

    @property
    def revisions(self):
        return self._revisions