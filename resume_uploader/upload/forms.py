from django import forms
from .models import Resume
import os

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['user', 'resume']
        labels = {'user': 'Name', 'resume': 'Resume'}

        #check if the file is pdf
        
    def clean_resume(self):
        resume = self.cleaned_data.get('resume', False)
        print("Resume",resume)
        if resume:
            ext = os.path.splitext(resume.name)[1]
            if ext.lower() != '.pdf':
                raise forms.ValidationError('Only PDF files are allowed')
        return resume
            