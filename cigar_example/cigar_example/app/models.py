from django.db import models



class Cigar(models.Model):
    COLOUR_CHOICES = (
        ("#f00", 'Red'),
        ('#0f0', 'Green'),
        ('#00f', 'Blue'),
    )

    name = models.CharField(max_length=25, help_text='Cigar Name')
    colour = models.CharField(max_length=30, choices = COLOUR_CHOICES, default="#0f0")
    gauge = models.IntegerField()
    length = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    notes = models.TextField()
    manufacturer = models.ForeignKey('Manufacturer')

    def get_absolute_url(self):
        return "/api/cigars/%i/" % self.id


class Manufacturer(models.Model):
    name = models.CharField(max_length=25)
    country = models.ForeignKey('Country')

    def __unicode__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=25, null=False, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"
