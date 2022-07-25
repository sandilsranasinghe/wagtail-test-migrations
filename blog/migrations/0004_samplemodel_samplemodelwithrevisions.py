# Generated by Django 4.0.3 on 2022-07-24 15:44

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0076_modellogentry_revision'),
        ('blog', '0003_alter_blogpage_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('stream_content', wagtail.fields.StreamField([('field1', wagtail.blocks.CharBlock()), ('quote', wagtail.blocks.StructBlock([('quote_content', wagtail.blocks.CharBlock()), ('person', wagtail.blocks.CharBlock()), ('random_id', wagtail.blocks.IntegerBlock(required=False))])), ('date', wagtail.blocks.DateTimeBlock()), ('someblock', wagtail.blocks.StructBlock([('random_content', wagtail.blocks.CharBlock()), ('random_date', wagtail.blocks.DateBlock(required=False))])), ('important_dates', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.CharBlock(required=False)), ('date', wagtail.blocks.DateBlock())])), ('somestreamblock', wagtail.blocks.StreamBlock([('title', wagtail.blocks.CharBlock()), ('content', wagtail.blocks.CharBlock())])), ('hpcharacters', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock()))], blank=True, use_json_field=True)),
            ],
        ),
        migrations.CreateModel(
            name='SampleModelWithRevisions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('stream_content', wagtail.fields.StreamField([('field1', wagtail.blocks.CharBlock()), ('quote', wagtail.blocks.StructBlock([('quote_content', wagtail.blocks.CharBlock()), ('person', wagtail.blocks.CharBlock()), ('random_id', wagtail.blocks.IntegerBlock(required=False))])), ('date', wagtail.blocks.DateTimeBlock()), ('someblock', wagtail.blocks.StructBlock([('random_content', wagtail.blocks.CharBlock()), ('random_date', wagtail.blocks.DateBlock(required=False))])), ('important_dates', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.CharBlock(required=False)), ('date', wagtail.blocks.DateBlock())])), ('somestreamblock', wagtail.blocks.StreamBlock([('title', wagtail.blocks.CharBlock()), ('content', wagtail.blocks.CharBlock())])), ('hpcharacters', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock()))], blank=True, use_json_field=True)),
                ('latest_revision', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='latest revision')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
