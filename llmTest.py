from openai import OpenAI

client=OpenAI(api_key='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',
              base_url='https://openrouter.ai/api/v1')

message=input("¿Cuál es tu pregunta?")
prompt=(
    "Por favor responde de manera clara, sin simbolos innecesarios."
    "Evita usar otros idiomas que no sea el castellano y escribe una respuesta concisa."
    f"Pregunta del usuario: {message}"
)

completion=client.chat.completions.create(
    model="cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
    messages=[
        {
            "role":"user",
            "content":prompt
        }
    ]
)
print(completion.choices[0].message.content)