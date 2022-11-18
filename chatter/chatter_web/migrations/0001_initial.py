# Generated by Django 4.1.3 on 2022-11-17 11:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a theme genre (e.g. Science Fiction)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False)),
                ('theme', models.TextField(blank=True, help_text='Enter your conversation theme', max_length=1000)),
                ('genre', models.ManyToManyField(help_text='Select a genre for this theme', to='chatter_web.genre')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]