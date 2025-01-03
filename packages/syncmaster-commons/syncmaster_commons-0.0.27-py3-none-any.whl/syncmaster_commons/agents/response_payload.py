from typing import Any, Union, override

from pydantic import Field

from syncmaster_commons.abstract.baseclass import (SMBaseClass,
                                                   ThirdPartyOutgoingPayload)
from syncmaster_commons.gupshup.agent_response_payload import \
    _AgentResponsePayloadGupshup


class AgentResponsePayload(SMBaseClass):
    """
    AgentResponsePayload class for handling agent request payloads.
    Attributes:
        agent_request_payload (Union[AgentResponsePayload]): The payload data for the agent request.
    Methods:
        from_dict(cls, response_payload: dict, client: str = None) -> "AgentResponsePayload":
            Creates an AgentResponsePayload object from a dictionary.
                request_payload (dict): The dictionary containing the payload data.
                client (str, optional): The client type. Defaults to None.
            Raises:
                ValueError If the client is not supported.
    """
    payload: Union[ThirdPartyOutgoingPayload,Any]

    @property
    def app_name(self) -> str:
        """
        Returns the name of the applicatio that the payload is associated with.
        """
        return self.payload.app_name
    
    @property
    def task_id(self) -> int:
        """
        Returns the task id.
        """
        return self.payload.task_id

    
    @override
    def to_dict(self):
        """
        Provides a dictionary representation of the current instance, extracted from
        the dictionary returned by the parent class.

        Returns:
            dict: The payload portion of the dictionary obtained from the parent class.
        """
        output_dict =  super().to_dict()
        return output_dict["payload"]
    

    @classmethod
    def from_dict(cls,response_payload: dict, client:str = None) -> "AgentResponsePayload":
        """
        Creates a AgentRequestPayload object from a dictionary.
        Args:
            payload_dict (dict): The dictionary containing the payload data.
        Returns:
            AgentRequestPayload: The AgentRequestPayload object created from the dictionary.
        """
        app_name = response_payload.get("app_name", None)
        if client == "WhatsApp" or app_name == "WhatsApp":
            payload = _AgentResponsePayloadGupshup.from_dict(response_payload) 
        else:
            raise ValueError(f"Client {client} is not supported.")
        return cls(
            payload=payload,
        )