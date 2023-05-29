import ssl
import smtplib

from email.message import EmailMessage
from fastapi.templating import Jinja2Templates

from app.core.constants import (
    EMAIL_USER,
    EMAIL_SUBJECT,
    EMAIL_SERVER,
    EMAIL_PASS,
    EMAIL_PORT,
    OK
)


class SendEmail:
    @staticmethod
    def to_send(request: dict, account_balance: dict) -> int:

        email_customer = request.get('email_customer')

        templates = Jinja2Templates(
            directory="app/core/templates"
        )

        context = {
            "request": request,
            "total": account_balance.get('total'),
            "debit": account_balance.get('debit'),
            "credit": account_balance.get('credit'),
            "months": account_balance.get('months'),
            "move": account_balance.get('move')
        }

        body = templates.TemplateResponse(
                 "email.html",
                 context
            )

        send = EmailMessage()
        send['From'] = EMAIL_USER
        send['To'] = email_customer
        send['Subject'] = EMAIL_SUBJECT
        send.add_header('Content-Type', 'text/html')
        send.set_payload(body.template.render(context))

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(
            EMAIL_SERVER,
            EMAIL_PORT,
            context=context
        ) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.sendmail(EMAIL_USER, email_customer, send.as_string())

        return OK
