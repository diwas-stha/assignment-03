

from abc import ABC, abstractmethod
class EmailSenderInterface(ABC):
    """
    Abstract base class representing an interface for sending emails.

    Methods:
        send_email(recipient: str, subject: str, message: str) -> None:
            Sends an email to the specified recipient.

    """
    @abstractmethod
    def send_email(self, recipient, subject, message):
        """
        Abstract method to send an email to the specified recipient.

        Parameters:
            recipient (str): The email address of the recipient.
            subject (str): The subject of the email.
            message (str): The content of the email.

        """
        pass

class EmailSender(EmailSenderInterface):
    """
    Class responsible for sending emails.

    Attributes:
        None

    Methods:
        send_email(recipient: str, subject: str, message: str) -> None:
            Sends an email to the specified recipient.

    """

    def send_email(self, recipient, subject, message):
        """
        Sends an email to the specified recipient.

        Parameters:
            recipient (str): The email address of the recipient.
            subject (str): The subject of the email.
            message (str): The content of the email.
        """
        # Code to send an email
        print(f"Sending email to {recipient}: {subject} - {message}")

class NotificationService:
    """
    Service class responsible for sending notifications.

    Attributes:
        email_sender (EmailSenderInterface): An object that implements the EmailSenderInterface.

    Methods:
        send_notification(recipient: str, message: str):
            Sends a notification to the specified recipient using the EmailSender.

    """

    def __init__(self, email_sender: EmailSenderInterface):
        """
        Initialize the NotificationService with an EmailSender.

        Parameters:
            email_sender (EmailSenderInterface): An object that implements the EmailSenderInterface. 
        """
        self.email_sender = email_sender

    def send_notification(self, recipient, message):
        """
        Sends a notification to the specified recipient using the EmailSender.

        Parameters:
            recipient (str): The email address of the recipient.
            message (str): The content of the notification.

        """
        self.email_sender.send_email(recipient, "Notification", message)

# Using the NotificationService to send a notification

if __name__ == "__main__":
    email_sender = EmailSender()
    notification_service = NotificationService(email_sender)
    notification_service.send_notification("user@example.com", "Hello, this is a notification!")
