class InterviewAgent:
    POOLS = {
        'python': ['What is a list comprehension?', 'Explain decorators.'],
        'django': ['What is Django ORM?', 'Explain middleware.'],
        'default': ['Tell me about yourself.', 'Why do you want this job?']
    }

    def execute(self, skill, user=None):
        return self.POOLS.get(skill.lower(), self.POOLS['default'])
