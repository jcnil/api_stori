from app.core.process import (
    EmailProcess
)


class EmailHandler:
    @staticmethod
    def register(request):
        obj = EmailProcess()
        return obj.register(request)

    @staticmethod
    def get_email(email_customer: str):
        obj = EmailProcess()
        return obj.get_email(email_customer)
