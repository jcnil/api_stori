from .models import (
    EmailModel
)


class Queryset:
    @staticmethod
    def get_account_balance_by_email(
        email_customer
    ) -> EmailModel:
        """
        Return a account based in email_customer.
        :param email_customer: str
        :return: EmailModel
        """
        return EmailModel.objects(
            email_customer=email_customer
        ).first()

    @staticmethod
    def create_row(request) -> EmailModel:
        """
        Create an document with data email
        :param request
        :return: EmailModel
        """
        customer = EmailModel.objects(
            email_customer=request.get('email_customer')
        ).first()

        if customer:
            customer.historical.append(dict(request))

        if not customer:
            customer = EmailModel(**request)
            customer.historical.append(dict(request))

        return customer.save()
