from django.shortcuts import render
from .forms import PasswordForm
import random
import string

# This view handles both GET and POST requests from the browser
def index(request):
    password = ''  # Default empty password to display in the template

    if request.method == 'POST':
        # The user submitted the form — Django captures the data in request.POST
        form = PasswordForm(request.POST)  # Bind form to submitted data

        if form.is_valid():
            # Extract cleaned data from the form
            length = form.cleaned_data['length']
            include_numbers = form.cleaned_data['include_numbers']
            include_special = form.cleaned_data['include_special']

            # Build character set based on user choices
            characters = string.ascii_letters
            if include_numbers:
                characters += string.digits
            if include_special:
                characters += string.punctuation

            # Generate password using random choices
            password = ''.join(random.choice(characters) for _ in range(length))

    else:
        # The user is just visiting the page — show an empty form
        form = PasswordForm()

    # Render the template with the form and password (if generated)
    return render(request, 'password_app/index.html', {
        'form': form,
        'password': password
    })
