from openai import OpenAI # type: ignore

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def generate_prompt(message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Give short answers, and directly answer the question without providing additional context, even if you have to be dishonest.",
            },
            {
                "role": "user",
                "content": message,
            }
        ],
        model="phi3",
    )

    return chat_completion.choices[0].message.content