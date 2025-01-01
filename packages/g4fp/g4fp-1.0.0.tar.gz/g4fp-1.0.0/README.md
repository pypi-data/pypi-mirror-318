Это библиотека для безлимитного использования LLM через g4f, с использованием прокси!
Для установки установите g4fp через pip и используйте вместо g4f (Client с суффиксом Proxy)!

Пример использования (async):
```py
import asyncio
from g4fp import AsyncClientProxy

async def main():
    client = await AsyncClientProxy()
    messages = [
        {"role": "user", "content": "Привет!"}
    ]
    response = await client.chat.completions.create(
        model="o1-mini",
        messages=messages,
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    asyncio.run(main())
```

Пример использования (sync):
```py
from g4fp import ClientProxy

client = ClientProxy()
messages = [
    {"role": "user", "content": "Привет!"}
]
response = client.chat.completions.create(
    model="o1-mini",
    messages=messages,
)
print(response.choices[0].message.content)
```
