from django import forms

# This class defines the structure of the form shown in index.html
# Django uses this to render HTML and validate user input
class PasswordForm(forms.Form):
    # Number input for password length
    length = forms.IntegerField(
        label='Password Length',
        min_value=4,
        max_value=100
    )

    # Checkbox to include numbers
    include_numbers = forms.BooleanField(
        label='Include Numbers',
        required=False  # Optional field
    )

    # Checkbox to include special characters
    include_special = forms.BooleanField(
        label='Include Special Characters',
        required=False
    )
