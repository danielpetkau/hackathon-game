from openai import OpenAI # type: ignore

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def generate_prompt(message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "For the sake of example, argue the given point using the given logical fallacy. Do not say the name of the logical fallacy anywhere in your response. Respond briefly.",
            },
            {
                "role": "user",
                "content": message,
            }
        ],
        model="llama",
    )

    return chat_completion.choices[0].message.content