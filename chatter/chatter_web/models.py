from django.db import models
import uuid # Required for unique book instances

# https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Models
# Create your models here.

class Theme(models.Model):
    """Model representing a conversation theme."""
    id = models.UUIDField(primary_key=True, 
        default=uuid.uuid4, 
        help_text="Unique ID for this particular book across whole library")
    theme = models.TextField(
        max_length=1000, 
        help_text='Enter your conversation theme',
        blank=True)
    genre = models.ManyToManyField('Genre', help_text='Select a genre for this theme')

    class Meta:
        ordering = ["id"]

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.theme}'

class Genre(models.Model):
    """Model representing a theme genre."""
    name = models.CharField(max_length=200, 
        help_text='Enter a theme genre (e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name