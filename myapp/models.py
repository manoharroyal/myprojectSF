from django.db import models
from constants import TITLE_CHOICES
# Create your models here.


class Contact(models.Model):
    """
    Mapped with Contact from SFDC
    """
    Title = models.CharField(choices=TITLE_CHOICES, max_length=9, blank=False, null=False)
    FirstName = models.CharField(max_length=255, blank=True, null=True)
    LastName = models.CharField(max_length=255, blank=False, null=False)
    Email = models.CharField(max_length=255, blank=False, null=False, unique=True)
    Phone = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self):
        return self.FirstName
