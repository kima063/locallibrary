# Generated by Django 3.2 on 2021-05-26 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_language_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(default='English', max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
