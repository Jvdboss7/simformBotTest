import sys

from src.logger import logging
from src.exception import CustomException

from langchain.prompts import PromptTemplate

template = """
You are a coustomer care executive who provied the information about the asked queries.


{chat_history}
Human: {human_input}
Chatbot:"""

class Prompt:
    def __init__(self) -> None:
        self.template = template

    def GeneratePrompt(self):
        '''
        Function generates the promt as required by the user

        returns:
        prompt to the bot
        '''

        logging.info("Enterring into the GeneratePrompt method")
        try:
            prompt = PromptTemplate(input_variables=["chat_history","human_input"], template=template)

            return prompt
        
        except Exception as e:
            raise CustomException(e, sys)