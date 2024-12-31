from typing import AsyncGenerator, Dict, Generator, List
import logging

from dictatorgenai.agents.general import General
from .base_conversation import BaseConversation

# Configuration du logger
logger = logging.getLogger(__name__)

class GroupChat(BaseConversation):
    async def start_conversation(
        self, dictator: General, generals: List[General], task: str
    ) -> AsyncGenerator[str, None]:
        """
        The dictator sends an imperative message to all the generals,
        validates their responses, and then uses the input to resolve the task.
        """
        try:
            # Step 1: Dictator initiates the task with an imperative message
            imperative_message = f"Dictator {dictator.my_name_is} commands: Solve the task '{task}'."
            logger.debug(f"Imperative message sent by Dictator {dictator.my_name_is}: {imperative_message}")

            # Step 2: Dictator sends the command to all generals and collects their responses
            responses = []
            for general in generals:
                try:
                    logger.debug(f"Sending command to General {general.my_name_is}...\n")
                    response_content = await dictator.send_message(general, imperative_message)
                    logger.debug(f"General {general.my_name_is}'s response: {response_content}\n")
                    # Structure the response as a dictionary
                    responses.append({"general": general.my_name_is, "content": response_content})
                except Exception as e:
                    logger.error(f"Error while communicating with General {general.my_name_is}: {e}")
                    responses.append({"general": general.my_name_is, "content": f"Error: {str(e)}"})

            # Step 3: Validate and combine responses
            logger.debug(f"Dictator {dictator.my_name_is} is analyzing the generals' responses...\n")
            validated_responses = self.validate_responses(responses)
            combined_response = self.compile_responses(validated_responses)
            logger.debug(f"Combined responses from generals: {combined_response}\n")

            # Step 4: Dictator uses the responses to finalize the task resolution
            logger.debug(f"Dictator {dictator.my_name_is} is now resolving the task based on the responses...\n")
            logger.info(f"{task} \n *** Generals' input below *** \n{combined_response}")
            async for chunk in dictator.solve_task(f"{task} \n *** Generals' input below *** \n{combined_response}"):
                yield chunk

        except Exception as e:
            logger.error(f"An error occurred during the conversation: {e}")
            yield f"An error occurred: {e}"

    def validate_responses(self, responses: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Validate and sanitize responses from generals.

        Args:
            responses (List[Dict[str, str]]): The raw responses from generals.

        Returns:
            List[Dict[str, str]]: A list of validated and sanitized responses.
        """
        validated = []
        for response in responses:
            if response.get("content") and "Error" not in response["content"]:
                validated.append(response)
            else:
                logger.warning(f"Invalid or empty response: {response}")
        return validated

    def compile_responses(self, responses: List[Dict[str, str]]) -> str:
        """
        Combine the responses from the generals into a structured decision.

        Args:
            responses (List[Dict[str, str]]): A list of dictionaries where each entry contains
                                              the name of the general and their response.

        Returns:
            str: A formatted string combining the responses, including the names of the generals.
        """
        formatted_responses = [
            f"{response['general']}: {response['content']}" for response in responses
        ]
        return "\n".join(formatted_responses)
