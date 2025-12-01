from core.models import Job

class JobSearchAgent:
    def execute(self, skills, user=None):
        if isinstance(skills, str):
            skills = [s.strip() for s in skills.split(',') if s.strip()]
        qs = Job.objects.all()
        matched = []
        for job in qs:
            job_skills = [s.strip().lower() for s in job.skills.split(',')] if job.skills else []
            if any(s.lower() in job_skills for s in skills):
                matched.append({'id': job.id, 'title': job.title, 'company': job.company, 'skills': job.skills})
        return matched
