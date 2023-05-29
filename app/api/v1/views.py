from pydantic.networks import EmailStr
from typing import Union, Annotated

from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse

from app.core.exceptions import (
    NotFoundException,
    ExistException
)
from app.core.handlers import (
    EmailHandler
)
from app.api.v1.serializers import (
    ResponseSerializer
)

router = APIRouter()


@router.post(
    "/send/account_balance",
    tags=["SendEmail"],
    response_model=ResponseSerializer
)
async def post_email(
    email_customer: Annotated[EmailStr, Form(...)],
    file: Union[UploadFile, None] = File(...)
) -> dict:
    """Post Email by specific customer about account balance"""
    try:
        request = {'email_customer': email_customer, 'filename': file.filename}

        result = EmailHandler.register(request)

        return JSONResponse(
            content={
                "status": result["status"],
                "data": result["data"],
                "message": str(result["message"])
            }
        )
    except ExistException as e:
        return JSONResponse(
            content={
                "status": e.status,
                "data": request,
                "message": str(e.message("Email")),
                "errors": str(e)
            },
            status_code=e.status
        )


@router.get(
    "/send//account_balance/{email_customer}",
    tags=["SendEmail"],
    response_model=ResponseSerializer
)
async def get_email(
    email_customer: str
):
    """Get Email by specific account"""
    try:
        result = EmailHandler.get_email(
            email_customer=email_customer
        )
        return JSONResponse(
            content={
                "status": result["status"],
                "data": result["data"],
                "message": str(result["message"])
            }
        )
    except NotFoundException as e:
        return JSONResponse(
            content={
                "status": e.status,
                "data": email_customer,
                "message": str(e.message("Email")),
                "errors": str(e)
            },
            status_code=e.status
        )
