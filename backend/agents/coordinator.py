from .job_search_agent import JobSearchAgent
from .resume_agent import ResumeAnalyzerAgent
from .interview_agent import InterviewAgent
from .application_agent import ApplicationAgent
from .notification_agent import NotificationAgent

class CoordinatorAgent:
    def __init__(self):
        self.job_agent = JobSearchAgent()
        self.resume_agent = ResumeAnalyzerAgent()
        self.interview_agent = InterviewAgent()
        self.application_agent = ApplicationAgent()
        self.notification_agent = NotificationAgent()

    def handle(self, request_type, data, user=None):
        if request_type == 'job':
            return self.job_agent.execute(data, user=user)
        if request_type == 'resume':
            return self.resume_agent.execute(data, user=user)
        if request_type == 'interview':
            return self.interview_agent.execute(data, user=user)
        if request_type == 'apply':
            res = self.application_agent.execute(data, user=user)
            # send notification
            try:
                self.notification_agent.send(user, 'Application submitted')
            except Exception:
                pass
            return res
        return {'error': 'unknown request type'}
