from core.models import Job, Application
from django.contrib.auth.models import User

class ApplicationAgent:
    def execute(self, data, user=None):
        # data expected: {'job_id': int}
        job_id = data.get('job_id') if isinstance(data, dict) else None
        if not job_id:
            return {'error': 'job_id required'}
        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            return {'error': 'job not found'}
        # If user provided, create application
        if user and user.is_authenticated:
            Application.objects.create(user=user, job=job, status='Applied')
            return {'message': f'Applied to {job.title}'}
        else:
            return {'message': 'User not authenticated. Application simulated.'}
