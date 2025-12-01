from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    skills = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} @ {self.company}"

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.IntegerField(default=0)
    extracted_skills = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"Resume {self.user.username}"

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Applied')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -> {self.job.title}"
