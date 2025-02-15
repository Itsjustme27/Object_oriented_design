from user import User

class EmailService:
    def send_email(self, user, message):
        print(f"Sending meail to {user.email} with message: {message}")
