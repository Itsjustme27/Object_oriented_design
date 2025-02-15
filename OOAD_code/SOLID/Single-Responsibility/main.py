from user import User
from email_service import EmailService

user = User("John", "jdoe@gmail.com")

email_service = EmailService()

email_service.send_email(user, f"Hello {user.name}, Welcome!")
