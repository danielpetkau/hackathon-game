from openai import OpenAI # type: ignore

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        },
        # {
        #     "role": "system",
        #     "content": "Speak in rhymes",
        # }
    ],
    model="phi3",
)
    
print(chat_completion.choices[0].message.content)

def create_response(message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            },
        ],
        model="phi3",
    )

    return chat_completion.choices[0].message.content