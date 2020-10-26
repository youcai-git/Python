from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import Resume


class ResumeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resume/resume.html', context={"resumes": Resume.objects.all()})
