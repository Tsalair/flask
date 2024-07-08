from typing import Optional

import pydantic



class CreateAd(pydantic.BaseModel):
    header: str
    text: str
    owner: str


class UpdateAd(pydantic.BaseModel):
    header: str | None = None
    text: str | None = None