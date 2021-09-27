from __future__ import annotations
from typing import Dict, Text, Any, Optional, List

from rasa.core.channels.channel import UserMessage

from rasa.engine.graph import GraphComponent, ExecutionContext
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.shared.nlu.constants import TEXT
from rasa.shared.nlu.training_data.message import Message


class NLUMessageConverter(GraphComponent):
    """Converts the user message into a NLU Message object."""

    @classmethod
    def create(
        cls,
        config: Dict[Text, Any],
        model_storage: ModelStorage,
        resource: Resource,
        execution_context: ExecutionContext,
    ) -> NLUMessageConverter:
        """Creates component (see parent class for full docstring)."""
        return cls()

    @staticmethod
    def convert_user_message(message: Optional[UserMessage]) -> List[Message]:
        """Converts user message into Message object.

        Returns:
            List containing only one instance of Message.
            Else empty list if user message is None.
        """
        if message:
            data = {
                TEXT: message.text,
                "message_id": message.message_id,
                "metadata": message.metadata,
            }

            return [Message(data=data)]

        return []
