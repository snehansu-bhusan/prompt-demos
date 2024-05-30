import openai
import gradio
import os

# Load environment variables

# Initialize OpenAI client
openai.api_key = "OPENAI_API_KEY"


messages = [{"role": "system", "content": "<Write your prommpt here>> "}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "<Write You Title/ Bot name here>")

demo.launch(share=True)
