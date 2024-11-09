from django.db import models


class Real_estate_property(models.Model):

    PROPERTY_TYPES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('land', 'Land'),
    ]

    address = models.CharField(max_length=100)
    price = models.IntegerField(max_digits=10)
    property_type = models.CharField(max_length=50)
    number_of_bedrooms = models.PositiveIntegerField()
    square_footage = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    property_image = models.ImageField(upload_to='property_images/')
    contact_details = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.property_type.capitalize()} - {self.address}"
