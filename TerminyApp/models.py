from django.db import models

# Create your models here.

class TerminyModel(models.Model):
    class Meta:
        db_table = 'TerminyTable'

    termin = models.TextField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.termin