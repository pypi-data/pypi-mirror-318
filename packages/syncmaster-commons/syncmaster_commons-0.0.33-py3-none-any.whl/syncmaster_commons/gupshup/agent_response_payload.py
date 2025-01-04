
from typing import override

from syncmaster_commons.abstract.baseclass import ThirdPartyOutgoingPayload
from syncmaster_commons.gupshup.outgoing_payloads import GupshupOutgoingPayload


class AgentResponsePayloadGupshup(ThirdPartyOutgoingPayload):
    """
    AgentResponsePayloadGupshup is a class that represents the payload for agent responses in the Gupshup integration.
    Attributes:
        outgoing_payload (GupshupOutgoingPayload): The outgoing payload object.
        task_id (str): The unique identifier for the task.

    Properties:
        app_name (str): Returns the name of the application.
        payload_type (str): Returns the incoming payload’s payload type.
        payload (dict): Constructs and returns the payload dictionary.
    Methods:
        from_dict(cls, payload_dict: dict) -> "AgentResponsePayloadGupshup":
    """
    outgoing_payload: GupshupOutgoingPayload
    
    @property
    def app_name(self) -> str:
        """
        Returns the name of the application.

        :return: The string 'gupshup'.
        :rtype: str
        """
        return self.outgoing_payload.app_name
    
    @property
    def payload_type(self) -> str:
        """
        Returns the incoming payload’s payload type.

        This property retrieves the type of the payload contained within the incoming payload,
        providing insight into how the payload should be processed or interpreted.

        Returns:
            str: The type of the payload.
        """
        return self.outgoing_payload.payload.type_text
    
    @property
    def payload(self) -> dict:
        """
        Constructs and returns the payload dictionary.
        This method retrieves the payload from the incoming payload object,
        converts it to a dictionary, and adds the payload type to the dictionary.
        Returns:
            dict: The payload dictionary with an added payload type.
        """
       
        payload = self.outgoing_payload.payload
        output_dict = payload.to_dict() 
        output_dict["payload_type"] = self.payload_type
        return output_dict

    @classmethod
    def from_dict(cls, payload_dict: dict) -> "AgentResponsePayloadGupshup":
        """
        Creates an instance of AgentResponsePayloadGupshup from a dictionary.
        Args:
            cls: The class itself.
            payload_dict (dict): A dictionary containing the payload data.
        Returns:
            AgentResponsePayloadGupshup: An instance of the class populated with data from the dictionary.
        Raises:
            KeyError: If 'task_id', 'user_id', or 'org_id' keys are missing in the payload_dict.
        """
        
        outgoing_payload = GupshupOutgoingPayload.from_dict(payload_dict["outgoing_payload"])
        print(outgoing_payload)        
        return cls(
            outgoing_payload=outgoing_payload,
            task_id=payload_dict["task_id"]            
            
        )