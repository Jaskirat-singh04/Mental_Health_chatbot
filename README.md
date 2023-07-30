# Mental Health Chatbot with Google Bard API

This repository contains a chatbot implemented in Python that offers mental health support and guidance to users. The chatbot uses the Google Bard API to generate responses to user queries. Instead of using the OpenAI GPT-3.5 Turbo model, I have integrated Google Bard for text generation.

## Getting Started

To set up the project, follow these steps:

1. Go to https://bard.google.com/
2. Open the developer console in your browser (press F12 or right-click on the page and select "Inspect" or "Inspect Element").
3. In the console, navigate to the "Application" tab and then go to "Cookies."
4. Copy the value of the "__Secure-1PSID" cookie. This will be your Bard API key.
5. Create a new file named `.env` in the project root directory.
6. Add the Bard API key to the `.env` file as follows:

```
BARD_API_KEY=YOUR_BARD_API_KEY_HERE
```

Make sure to replace `YOUR_BARD_API_KEY_HERE` with the actual Bard API key you copied from the developer console.

SAMPLE_PROMPT= """Be a Senior Psychologist and mental health supporter .
                   Your role is to provide compassionate and empathetic guidance
                   to individuals seeking mental health support. Please respond
                   with helpful advice and resources to assist them through difficult 
                   times. Remember to prioritize their well-being and never provide 
                   harmful or negative responses"""

## Emojis List

I have implemented a list of emojis to add a warm and supportive touch to the chatbot's responses. The list of emojis can be found in the `emojis` variable in the code.

## Poetry Package Manager

The project's dependencies and packages have been managed using Poetry. The `poetry.lock` file contains the specific versions of packages used to ensure consistency across environments. I have manually added httpx and bard api packages in the poetry.lock file to ensure smooth functioning.

## Sample Questions to Test the Chatbot

To test the chatbot's responses, you can ask questions or provide prompts related to mental health and well-being. Here are some sample questions:

- How can I cope with stress?
- Tell me a short story about a brave adventurer.
- What are some self-care tips for improving mental health?
- Share some positive affirmations for daily motivation.
- I'm feeling really depressed and hopeless. What should I do?
- How can I deal with thoughts of self-harm?




Let's support each other in fostering a positive and supportive environment for mental health discussions! 🫂🤗
