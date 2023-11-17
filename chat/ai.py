from config import token
import openai
from db.MySqlConn import config

OPENAI_CHAT_COMPLETION_OPTIONS = {
    "temperature": 0.7,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "stream": True,
    "stop": None
}


async def ChatCompletionsAI(logged_in_user, messages) -> (str, str):
    level = logged_in_user.get("level")

    # Setup AI
    openai.api_key = config["AI"]["TOKEN"]
    OPENAI_CHAT_COMPLETION_OPTIONS["model"] = "gpt-3.5-turbo"
    response = await openai.ChatCompletion.acreate(
        messages=messages,
        max_tokens=token[level],
        **OPENAI_CHAT_COMPLETION_OPTIONS)

    answer = ""
    async for r in response:
        delta = r.choices[0].delta
        answer += delta["content"] if delta.get("content") else ""
        yield answer, r.choices[0]["finish_reason"]
