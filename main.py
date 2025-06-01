import os
from dotenv import load_dotenv
import chainlit as cl
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from typing import Optional, Dict
from agents.tool import function_tool

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)

# Agent for translation
agent = Agent(
    name="Translator Agent",
    instructions="""
You are a language translation assistant. Your job is to translate text from one language to another. 
When the user sends a message, you should detect the input language and ask the user which language they want the text translated into (if not already specified).

Examples:
- If the user says: 'Translate "Hello" to Spanish' → respond with 'Hola'.
- If user just says: 'Bonjour' → detect it's French and ask: "What language would you like to translate this to?"

You support these languages: English, Urdu, Spanish, French, German, Arabic, Hindi, Chinese.

If the request is unclear or unsupported, politely ask for clarification.
""",
    model=model,
    tools=[],
)

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content=" Welcome to Muskan's Translator Bot! Type anything you'd like to translate.").send()

@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})

    result = await cl.make_async(Runner.run_sync)(agent, history)

    response_text = result.final_output

    await cl.Message(content=response_text).send()

    history.append({"role": "assistant", "content": response_text})
    cl.user_session.set("history", history)
