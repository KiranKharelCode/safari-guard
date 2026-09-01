from groq import Groq
from osscripts import ai_prompt

key = "YOUR API KEY HERE"

client = Groq(
    api_key=key
)



def reasoning(sites):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user","content": f"{ai_prompt()}, {sites}",}],model="openai/gpt-oss-120b")


    return(chat_completion.choices[0].message.content)
