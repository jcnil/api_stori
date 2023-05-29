from typing import Optional, Union

from pydantic import BaseModel, Field


class ResponseSerializer(BaseModel):
    status: Optional[str] = Field(
        title="Status Code",
    )
    data: Optional[dict] = Field(
        title="Response data",
    )
    message: Optional[str] = Field(
        title="Complementary message",
    )
    errors: Optional[Union[dict, list]] = Field(
        title="Retrieves a list of errors if an action fails",
    )


class MetaDataSerializer(BaseModel):
    credit_request_uid: str = Field(
        title="Credit Request Uid"
    )
    url: str = Field(
        title="Public url of the file"
    )
