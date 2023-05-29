import glob

from app.core.exceptions import NotFoundException
from app.core.querysets import Queryset
from app.core.balance import AccountBalance
from app.core.send import SendEmail
from app.core.constants import OK


class EmailProcess:
    @staticmethod
    def register(request: dict) -> dict:
        """
        this function record and send email customer
        :param request:
        :return: response dictionary
        """

        filepath = glob.glob(f"**/{request.get('filename')}", recursive=True)

        request['path'] = filepath[0]

        request['account_balance'] = AccountBalance.account_balance(request)

        SendEmail.to_send(request, request['account_balance'])

        Queryset.create_row(request)

        return {
            "status": OK,
            "message": "Registered",
            "data": request
        }

    @staticmethod
    def get_email(email_customer: str) -> dict:
        """
        this function record user verification
        steps and publish in a sns
        :param request: email_customer
        :return: response dictionary
        """
        email = Queryset.get_account_balance_by_email(
            email_customer=email_customer
        )

        if email is not None:
            return {
                "status": OK,
                "message": "Exist email of customer in Local Database",
                "data": {
                    "email_customer": email.email_customer,
                    "historical": email.historical
                }
            }
        raise NotFoundException
