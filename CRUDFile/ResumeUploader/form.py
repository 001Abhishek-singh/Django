from ResumeUploader.models import resumeModel
from django import forms

class ResumeForm(forms.ModelForm):
    class Meta:
        model = resumeModel
        fields = '__all__'
        labels = {'userName':'Full Name','userSurname':'Surname','userContact':'Contact No','userEmail':'Email ID :','DoB':'Date-of-Birth','profileImage':'Upload Image','resumeHoleder':'Upload Resume'}
        