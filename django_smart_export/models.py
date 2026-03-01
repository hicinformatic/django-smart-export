from django.db import models


class ExampleModel(models.Model):
    """Example model for testing export functionality."""

    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        """Return string representation of the model."""
        return self.name
