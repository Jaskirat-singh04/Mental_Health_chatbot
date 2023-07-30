import textbase
from textbase.message import Message
from textbase import models
from dotenv import load_dotenv, find_dotenv
import os
from typing import List
from bardapi import Bard
import random


emojis = ["🫂", "🤗", "😊", "❤️", "🌟", "🪄", "🌸", "😀", "🍀", "🙌"]
# Prompt for Bard to initialize role.
SYSTEM_PROMPT = """ Be a Senior Psychologist and mental health supporter .
                   Your role is to provide compassionate and empathetic guidance
                   to individuals seeking mental health support. Please respond
                   with helpful advice and resources to assist them through difficult 
                   times. Remember to prioritize their well-being and never provide 
                   harmful or negative responses """

#generate text
def call_bard(scenerio):
   bard = Bard()
   template=scenerio
   answer = bard.get_answer(template)
#    return (answer['content'])
   sentence_ending_punctuation = [".", "!", "?"]
   spaced_content = answer['content']
   for punctuation in sentence_ending_punctuation:
    spaced_content = spaced_content.replace(punctuation, punctuation + "\n")
    return spaced_content
    

@textbase.chatbot("talking-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Your chatbot logic here
    message_history: List of user messages
    state: A dictionary to store any stateful information

    Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
    """

    if state is None or "counter" not in state:
        state = {"counter": 0}
    else:
        state["counter"] += 1
    
    

    # Concatenate user messages to create a scenario
    scenario = "\n".join(message.content for message in message_history)


    # If it's the first message from the user, greet them with the initial message
    if state["counter"] == 0:
        call_bard(SYSTEM_PROMPT)
        bot_response = "Hello there 👋 I'm here to offer you mental health supportand guidance. Feel free to share your thoughts and feelings with me🧙. I'm here to listen and provide assistance to help you navigate through any challenges you may be facing. Remember, your well-being is my top priority, and I'm here to support you in a safe and caring environment. How can I assist you today? 😊"
    else:
        # Call Google Bard function (template-based) for the user's input
        bot_response = call_bard(scenario)
        bot_response += " " + random.choice(emojis)

    return bot_response, state
