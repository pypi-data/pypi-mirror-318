from collections.abc import Mapping
from typing import Any

from pydantic import BaseModel, ConfigDict
from requests import HTTPError
from slack_sdk.web import SlackResponse as SlackResponseSDK


class BaseResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
    ok: bool

    def __getitem__(self, key: str) -> Any:
        if self.model_extra and key in self.model_extra:
            return self.model_extra[key]
        return getattr(self, key)

    def __setitem__(self, key: str, value: Any):
        if not self.model_extra:
            setattr(self, key, value)
        else:
            self.model_extra[key] = value

    def __len__(self):
        return len(self.__dict__) + (len(self.model_extra) if self.model_extra else 0)


class ErrorResponse(BaseResponse):
    error: str

    def raise_error(self):
        raise HTTPError(f"Slack API error: {self.error}")


class WarningResponse(BaseResponse):
    warning: str

    def raise_warning(self):
        raise RuntimeWarning(f"Slack API warning: {self.warning}")


class SlackResponse(BaseResponse):
    @classmethod
    def from_(
        cls, response: SlackResponseSDK | dict[str, Any] | bytes
    ) -> "SlackResponse":
        if isinstance(response, SlackResponseSDK):
            response = response.data

        if isinstance(response, bytes):
            from json import loads

            response = loads(response)

        if isinstance(response, SlackResponse):
            return response

        if not isinstance(response, Mapping):
            raise ValueError("Invalid response type")

        if response.get("warning"):
            WarningResponse(**response).raise_warning()
        elif response.get("error"):
            ErrorResponse(**response).raise_error()
        else:  # response.get("ok")
            return cls(**response)

    def __add__(self, other: "BaseResponse") -> "SlackResponse":
        return self.__class__(**self.model_dump(), **other.model_dump())
