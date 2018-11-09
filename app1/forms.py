from django import forms
from app1.models import Student

class StudentForm(forms.ModelForm):
    class Meta():
        model=Student
        fields=('__all__')

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['enquiary_date'].label = "Enquiary Date*(Enquiary form ends here-------------------)"
        self.fields['city'].label = "City/District"
        self.fields['college'].label='College(Refrence)'
        self.fields['name'].label = "Name*"
        self.fields['email'].label = 'Email*'
        self.fields['mobile'].label = "Mobile No.*"
        self.fields['course'].label = 'Course*'
        self.fields['student_status'].label = "Student_status*"



