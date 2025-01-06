from send_2_llm import LLMClient

async def main():
    # Создаем клиент - это все что нужно для начала работы
    client = LLMClient()
    
    # Простой пример использования
    response = await client.generate("Напиши короткое хайку о весне")
    print(f"Ответ LLM:\n{response}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main()) 