class ResumeAnalyzerAgent:
    KEY_SKILLS = ['python','django','mysql','ai','ml','nlp','javascript','react']

    def execute(self, resume_text, user=None):
        text = resume_text.lower() if isinstance(resume_text, str) else ''
        found = [s for s in self.KEY_SKILLS if s in text]
        score = min(100, len(found) * 20)
        return {'skills_found': found, 'score': score}
