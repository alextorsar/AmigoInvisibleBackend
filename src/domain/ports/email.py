from abc import ABC, abstractmethod

class IEmailService(ABC):
    """Interface for sending emails."""

    @abstractmethod
    async def send_email(
        self,
        to_email: str,
        subject: str,
        body: str,
        to_name: str = ""
    ) -> bool:
        """
        Sends an email asynchronously to the designated recipient.
        
        Args:
            to_email: The recipient's email address.
            subject: The subject line of the email.
            body: The email content (can support basic text or HTML).
            to_name: Optional recipient name for personalization.
            
        Returns:
            True if the email was sent successfully, False otherwise.
        """
        pass
