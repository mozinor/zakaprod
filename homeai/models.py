from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Contact(models.Model):
    firstname = models.CharField(max_length=70)
    lastname = models.CharField(max_length=70)
    contact_email = models.EmailField()
    email_copy = models.BooleanField(default=False)
    email_content = models.CharField(max_length=700)
    contact_date = models.DateTimeField('contact_date')

    def __str__(self):
        return self.contact_firstname + ' '+ self.contact_lastname

