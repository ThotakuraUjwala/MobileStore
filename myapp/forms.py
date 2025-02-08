from django import forms
from .models import Mobiles, Laptops, Brand, LapBrand

class DeviceRecommendationForm(forms.Form):
    CATEGORY_CHOICES = [('Mobile', 'Mobile'), ('Laptop', 'Laptop')]
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='What are you looking for?')
    budget = forms.IntegerField(label='What is your budget?')
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), required=False, label='Preferred Mobile Brand')
    laptop_brand = forms.ModelChoiceField(queryset=LapBrand.objects.all(), required=False, label='Preferred Laptop Brand')
    battery = forms.CharField(max_length=100, required=False, label='Battery Preference')
    ram = forms.CharField(max_length=30, required=False, label='RAM Preference')
    processor = forms.CharField(max_length=100, required=False, label='Processor Preference')