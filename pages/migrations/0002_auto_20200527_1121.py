# Generated by Django 2.2.5 on 2020-05-27 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['order', 'title'], 'verbose_name': 'página', 'verbose_name_plural': 'páginas'},
        ),
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.SmallIntegerField(default=0, verbose_name='Orden'),
        ),
    ]
