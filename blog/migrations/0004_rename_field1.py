# Generated by Django 4.0.4 on 2022-06-05 10:05

from django.db import migrations
from wagtail.fields import StreamField


def forward(apps, schema_editor):
    BlogPage = apps.get_model("blog", "BlogPage")
    model_field_name = "content"
    old_name = "field1"
    new_name = "block1"

    curr_field = BlogPage._meta.get_field(model_field_name)
    all_blocks = []
    for key, value in curr_field.stream_block.child_blocks.items():
        path, args, kwargs = value.deconstruct()
        if key == new_name:
            all_blocks.append((old_name, value.__class__(*args, **kwargs)))
            all_blocks.append((new_name, value.__class__(*args, **kwargs)))
        else:
            all_blocks.append((key, value.__class__(*args, **kwargs)))
    all_fields = StreamField(all_blocks)
    all_fields.contribute_to_class(BlogPage, model_field_name)

    # change the streamfield so that it has both blocks now
    schema_editor.alter_field(BlogPage, curr_field, all_fields)

    for page in BlogPage.objects.all():
        stream_blocks = getattr(page, model_field_name)
        for index, child in enumerate(stream_blocks):
            if child.block_type == old_name:
                stream_blocks[index] = (new_name, child.value)
        setattr(page, model_field_name, stream_blocks)
        page.save()

    # change the streamfield back to how it was
    schema_editor.alter_field(BlogPage, all_fields, curr_field)


def backward(apps, schema_editor):
    BlogPage = apps.get_model("blog", "BlogPage")
    model_field_name = "content"
    old_name = "field1"
    new_name = "block1"

    curr_field = BlogPage._meta.get_field(model_field_name)
    all_blocks = []
    for key, value in curr_field.clone().stream_block.child_blocks.items():
        path, args, kwargs = value.deconstruct()
        if key == new_name:
            all_blocks.append((old_name, value.__class__(*args, **kwargs)))
            all_blocks.append((new_name, value.__class__(*args, **kwargs)))
        else:
            all_blocks.append((key, value.__class__(*args, **kwargs)))
    all_fields = StreamField(all_blocks)
    all_fields.contribute_to_class(BlogPage, model_field_name)

    # change the streamfield so that it has both blocks now
    schema_editor.alter_field(BlogPage, curr_field, all_fields)

    for page in BlogPage.objects.all():
        stream_blocks = getattr(page, model_field_name)
        for index, child in enumerate(stream_blocks):
            if child.block_type == new_name:
                stream_blocks[index] = (old_name, child.value)
        setattr(page, model_field_name, stream_blocks)
        page.save()

    # change the streamfield back to how it was
    schema_editor.alter_field(BlogPage, all_fields, curr_field)


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_blogpage_content"),
    ]

    operations = [migrations.RunPython(forward, backward)]
