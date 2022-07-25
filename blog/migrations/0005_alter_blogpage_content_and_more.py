# Generated by Django 4.0.3 on 2022-07-24 15:45

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_samplemodel_samplemodelwithrevisions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='content',
            field=wagtail.fields.StreamField([('block1', wagtail.blocks.CharBlock()), ('quote', wagtail.blocks.StructBlock([('quote_content', wagtail.blocks.CharBlock()), ('author', wagtail.blocks.CharBlock()), ('random_id', wagtail.blocks.IntegerBlock(required=False))])), ('date', wagtail.blocks.DateTimeBlock()), ('someblock', wagtail.blocks.StructBlock([('random_content', wagtail.blocks.CharBlock()), ('random_date', wagtail.blocks.DateBlock(required=False))])), ('important_dates', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.CharBlock(required=False)), ('date', wagtail.blocks.DateBlock())])), ('somestreamblock', wagtail.blocks.StreamBlock([('title', wagtail.blocks.CharBlock()), ('content', wagtail.blocks.CharBlock())])), ('hpcharacters', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock()))], blank=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='samplemodel',
            name='stream_content',
            field=wagtail.fields.StreamField([('block1', wagtail.blocks.CharBlock()), ('quote', wagtail.blocks.StructBlock([('quote_content', wagtail.blocks.CharBlock()), ('author', wagtail.blocks.CharBlock()), ('random_id', wagtail.blocks.IntegerBlock(required=False))])), ('date', wagtail.blocks.DateTimeBlock()), ('someblock', wagtail.blocks.StructBlock([('random_content', wagtail.blocks.CharBlock()), ('random_date', wagtail.blocks.DateBlock(required=False))])), ('important_dates', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.CharBlock(required=False)), ('date', wagtail.blocks.DateBlock())])), ('somestreamblock', wagtail.blocks.StreamBlock([('title', wagtail.blocks.CharBlock()), ('content', wagtail.blocks.CharBlock())])), ('hpcharacters', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock()))], blank=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='samplemodelwithrevisions',
            name='stream_content',
            field=wagtail.fields.StreamField([('block1', wagtail.blocks.CharBlock()), ('quote', wagtail.blocks.StructBlock([('quote_content', wagtail.blocks.CharBlock()), ('author', wagtail.blocks.CharBlock()), ('random_id', wagtail.blocks.IntegerBlock(required=False))])), ('date', wagtail.blocks.DateTimeBlock()), ('someblock', wagtail.blocks.StructBlock([('random_content', wagtail.blocks.CharBlock()), ('random_date', wagtail.blocks.DateBlock(required=False))])), ('important_dates', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.CharBlock(required=False)), ('date', wagtail.blocks.DateBlock())])), ('somestreamblock', wagtail.blocks.StreamBlock([('title', wagtail.blocks.CharBlock()), ('content', wagtail.blocks.CharBlock())])), ('hpcharacters', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock()))], blank=True, use_json_field=True),
        ),
    ]
