from django import forms
from .models import Real_estate_property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Real_estate_property
        fields = [
            'address', 'price', 'property_type', 'number_of_bedrooms',
            'square_footage', 'location', 'property_image', 'contact_details'
        ]