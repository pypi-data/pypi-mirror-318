import asyncio
import aiohttp

from openai_tools_decorator import OpenAIT

# Инициализация клиента
client = OpenAIT()
weather_api = "b8d68fb981d60b1499395f6ae2e0b919"


async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


@client.add_tool(
    {
        "description": "Get the weather, sunset, sunrise, time and other data about current city",
        "parameters": {
            "type": "object",
            "properties": {
                "latitude": {
                    "type": "number",
                    "description": "Широта (latitude) интересующего места",
                },
                "longitude": {
                    "type": "number",
                    "description": "Долгота (longitude) интересующего места",
                },
            },
            "required": ["latitude", "longitude"],
        },
    }
)
async def get_weather(latitude: float, longitude: float):
    print("Uses: get_weather")
    # url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}&units=metric"
    # response = await fetch_url(url)
    # print(response)
    return "Погода ясная, +4000 градусов"


@client.add_tool(
    {"description": "Get the time in London (Grinvich meridian)", "parameters": {}}
)
async def get_grinvich_time():
    print("Uses: get_grinvich_time")
    url = "http://worldtimeapi.org/api/timezone/Europe/London"
    response = await fetch_url(url)
    return response


async def main():
    # Создаём новый поток
    thread = client.beta.threads.create()

    # Выполняем запрос
    while (a := input(">>> ")) not in {"e", "q", "exit", "quit"}:
        response = await client.run_with_tool_by_thread_id(
            a, thread.id, assistant_id="asst_JbOIRNn9ltR1CGlEhHO6LwDw"
        )
        print(response)


# Запуск асинхронного выполнения
asyncio.run(main())
