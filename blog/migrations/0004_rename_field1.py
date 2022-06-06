# Generated by Django 4.0.4 on 2022-06-06 17:53

import json
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
        if key == new_name:
            all_blocks.append((old_name, value.__class__()))
            all_blocks.append((new_name, value.__class__()))
        else:
            all_blocks.append((key, value.__class__()))
    all_fields = StreamField(all_blocks)
    all_fields.contribute_to_class(BlogPage, model_field_name)

    # change the streamfield so that it has both blocks now
    schema_editor.alter_field(BlogPage, curr_field, all_fields)

    for bp in BlogPage.objects.all():
        for index, child in enumerate(getattr(bp, model_field_name)):
            if child.block_type == old_name:
                getattr(bp, model_field_name)[index] = (new_name, child.value)
        bp.save()

        for revision in bp.revisions.all():
            stream_data = []
            mapped = False

            for block in json.loads(revision.content["content"]):
                if block["type"] == "field1":
                    new_block = {}
                    new_block["type"] = "block1"
                    new_block["value"] = block["value"]
                    stream_data.append(new_block)
                    mapped = True

                else:
                    stream_data.append(block)

            if mapped:
                revision.content["content"] = json.dumps(stream_data)
                revision.save()

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
        if key == new_name:
            all_blocks.append((old_name, value.__class__()))
            all_blocks.append((new_name, value.__class__()))
        else:
            all_blocks.append((key, value.__class__()))
    all_fields = StreamField(all_blocks)
    all_fields.contribute_to_class(BlogPage, model_field_name)

    # change the streamfield so that it has both blocks now
    schema_editor.alter_field(BlogPage, curr_field, all_fields)

    for bp in BlogPage.objects.all():
        for index, child in enumerate(getattr(bp, model_field_name)):
            if child.block_type == new_name:
                getattr(bp, model_field_name)[index] = (old_name, child.value)
        bp.save()

        for revision in bp.revisions.all():
            stream_data = []
            mapped = False

            for block in json.loads(revision.content["content"]):
                if block["type"] == "block1":
                    new_block = {}
                    new_block["type"] = "field1"
                    new_block["value"] = block["value"]
                    stream_data.append(new_block)
                    mapped = True

                else:
                    stream_data.append(block)

            if mapped:
                revision.content["content"] = json.dumps(stream_data)
                revision.save()

    # change the streamfield back to how it was
    schema_editor.alter_field(BlogPage, all_fields, curr_field)


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_blogpage_content"),
    ]

    operations = [
        migrations.RunPython(forward, backward)
    ]
