import chainlit as cl
import aiapi
from langchain.prompts import PromptTemplate
from src.api.prompt import Prompt

abc=0
prompt = Prompt().GeneratePrompt()
@cl.on_message
async def main(message: str):
    """
    The `main` function takes a message as input and generates a chat response using an AI model.
    
    :param message: The `message` parameter is a string that represents the user's input or message. It
    is used as input for generating a chat response using the `aiapi.generateChatResponse()` function
    :type message: str
    """
    global abc 
    # global prompt
    if abc == 0:
        prompts = message
        query = prompt.format(human_input= prompts, chat_history= [])
        abc = 1
        answer= aiapi.generateChatResponse(query)
    else:
        prompts = message
        answer= aiapi.generateChatResponse(prompts)

    await cl.Message(
        content=f"{answer}",
    ).send()
