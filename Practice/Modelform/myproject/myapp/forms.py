from django.forms import ModelForm
from myapp.models import *

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
