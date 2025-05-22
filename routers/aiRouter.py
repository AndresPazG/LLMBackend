from fastapi import APIRouter
from openai import OpenAI
from Interface.chatInterfaces import InputMessage, ChatCompletionResponse

router=APIRouter()
client=OpenAI(api_key='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',
              base_url='https://openrouter.ai/api/v1')

@router.post("/ai-chat")
def aiChat(data: InputMessage):
    data=data.model_dump()
    print("Message "+ data["message"])

    prompt="Por favor responde de manera clara, concreta y siempre en castellano"

    try:
        completion: ChatCompletionResponse =client.chat.completions.create(
            model="google/gemma-3-1b-it:free",
            messages=[
                {
                    "role":"system",
                    "content":"Eres un asistente que siempre respondes en castellano o español de forma clara y breve"
                },
                {
                    "role":"user",
                    "content": prompt+ "responde a esta pregunta: "+data["message"]
                }
            ]
        )
        print("responde " + completion.choices[0].message.content)
        return {"response":completion.choices[0].message.content}
    except Exception as e:
        print(f"Error: {e}")
        return {"error":str(e)}

#DeepSeek
@router.post("/ai-chat-deepseek")
def aiChatDeepSeek(data: InputMessage):
    data=data.model_dump()
    print("Message "+ data["message"])

    prompt="Por favor responde de manera clara, concreta y siempre en castellano"

    try:
        completion: ChatCompletionResponse =client.chat.completions.create(
            model="deepseek/deepseek-prover-v2:free",
            messages=[
                {
                    "role":"system",
                    "content":"Eres un asistente que siempre respondes en castellano o español de forma clara y breve"
                },
                {
                    "role":"user",
                    "content": prompt+ "responde a esta pregunta: "+data["message"]
                }
            ]
        )
        print("responde " + completion.choices[0].message.content)
        return {"response":completion.choices[0].message.content}
    except Exception as e:
        print(f"Error: {e}")
        return {"error":str(e)}