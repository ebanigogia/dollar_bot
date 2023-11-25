import unittest
from unittest.mock import patch
from code.notification import send_email_notification
import smtplib

class TestSendEmailNotification(unittest.TestCase):

    @patch('smtplib.SMTP')
    def test_send_email_success(self, mock_smtp):
        # Test the successful email sending without any exceptions
        subject = "Test Subject"
        message = "This is a test message."

        instance = mock_smtp.return_value
        instance.starttls.return_value = True
        instance.login.return_value = True

        send_email_notification(subject, message)

        instance.sendmail.assert_called_once()

if __name__ == '__main__':
    unittest.main()
