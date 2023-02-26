from django.shortcuts import render
from .models import Resume
from .forms import ResumeForm
from django.views import View
from django.http import HttpResponseRedirect
import os

# Create your views here.
class ResumeView(View):
  
    def get(self, request):
        form = ResumeForm()
        return render(request, 'upload/resume_form.html', {'form': form})
    
    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            # print("Cleaned_data: ", cleaned_data)
            # print("Request.files : ", request.FILES)
            # resume = cleaned_data['resume']
            # ext = os.path.splitext(resume.name)[1]
            # print(ext)
            form.save()
            form = ResumeForm()
       
            
        return render(request, 'upload/resume_form.html', {'form': form})
    
# do the abpve thing using list view