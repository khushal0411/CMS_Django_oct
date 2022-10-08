from django.db import models

# Create your models here.
class OrgData(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=10)
    phone = models.CharField('Contact', max_length=11)
    web = models.URLField('Website')
    email = models.EmailField('E-mail')

    def __str__(self):
        return self.name
