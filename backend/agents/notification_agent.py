class NotificationAgent:
    def send(self, user, message):
        # Simple placeholder: in real app, integrate email or push
        return {'to': getattr(user, 'username', 'anonymous'), 'message': message}
