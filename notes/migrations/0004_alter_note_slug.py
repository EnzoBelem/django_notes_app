# Generated by Django 4.1.7 on 2023-03-26 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_remove_note_cover_note_card_cover_note_page_cover_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
