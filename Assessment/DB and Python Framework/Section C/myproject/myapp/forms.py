from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile

        fields = [
            'username',
            'age',
            'email',
            'is_public'
        ]

    def clean_age(self):

        age = self.cleaned_data['age']

        if age < 13:
            raise forms.ValidationError(
                "Age must be at least 13."
            )

        return age