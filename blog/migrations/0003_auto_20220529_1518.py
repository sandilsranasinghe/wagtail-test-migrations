# Generated by Django 4.0.4 on 2022-05-29 15:18

from django.db import migrations
from wagtail.blocks import StreamValue


def forward(apps, schema_editor):
    BlogPage = apps.get_model("blog", "BlogPage")

    for bp in BlogPage.objects.all():
        stream_data = []
        mapped = False
        list_block_values = []

        for block in bp.content.get_prep_value():
            if block["type"] == "field1":
                mapped = True
                new_block = {}
                new_block["type"] = "item"
                new_block["value"] = block["value"]
                list_block_values.append(new_block)

            else:
                stream_data.append(block)

        if mapped:
            new_block = {}
            new_block["type"] = "field1"
            new_block["value"] = list_block_values
            stream_data.append(new_block)

            stream_block = bp.content.stream_block
            bp.content = StreamValue(stream_block, stream_data, is_lazy=True)
            bp.save()


def backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_blogpage_content"),
    ]

    operations = [
        migrations.RunPython(forward, backward)
    ]