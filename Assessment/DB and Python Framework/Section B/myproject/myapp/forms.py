from django import forms

class UserProfileForms(forms.Form):
    username = forms.CharField(max_length=100,label="Username")
    age = forms.IntegerField(label="Age")
    is_public = forms.BooleanField(required=False,initial=True,label="Public Profile")

    #custom Validation

    def clean_age(self):
        age = self.cleaned_data.get("age")

        if age < 13:
            raise forms.ValidationError("User must be at least 13 years old.")
        return age
        