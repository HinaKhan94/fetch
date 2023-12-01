from django import forms
from .models import Product, Category, Review
from django.core.validators import (
    MaxValueValidator, MinValueValidator
)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """
    Form for Review Model - Add / Edit
    """

    class Meta:
        model = Review
        fields = ('content', 'rating',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Sets placeholder values
        placeholders = {
            'content': 'Your Review',
            'rating': 0
        }

        # Sets autofocus on first input
        self.fields['content'].widget.attrs['autofocus'] = True

        # Sets aria-labels on inputs
        self.fields['content'].widget.attrs['aria-label'] = 'Review Content'
        self.fields['rating'].widget.attrs[
            'aria-label'] = 'Rating: Choose a value between 1-5'

        for field in self.fields:
            # Sets placeholders on fields with * for required fields
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]

            # Sets placeholders on inputs
            self.fields[field].widget.attrs['placeholder'] = placeholder

            # Adds stylings classes to inputs
            self.fields[field].widget.attrs['class'] = (
                'ib-form-field mb-3 px-2 py-2 font-body text-dark-grey')

            # Removes input labels
            self.fields[field].label = False

            # Add validators to the rating field
        self.fields['rating'].validators.append(MinValueValidator(0))
        self.fields['rating'].validators.append(MaxValueValidator(5))