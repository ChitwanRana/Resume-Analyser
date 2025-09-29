from django.db import models

class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    career_field = models.CharField(max_length=100, blank=True)
    resume_score = models.FloatField(blank=True, null=True)
    skills_missing = models.TextField(blank=True)
    recommended_courses = models.TextField(blank=True)

    def __str__(self):
        return f"{self.file.name}"
