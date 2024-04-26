from openai import OpenAI # type: ignore

api_key = "sk-proj-uKBt9syTrOBcCtkW107AT3BlbkFJ5veseUervdY2Y6Z1IWh1"
client = OpenAI(api_key=api_key)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion.choices[0].message.content)