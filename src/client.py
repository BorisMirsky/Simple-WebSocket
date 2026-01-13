
import random
import websockets
import asyncio
from faker import Faker
from faker.providers.person.ru_RU import Provider
from websockets.asyncio.client import connect



# создание объекта Faker с локализацией для России
fake = Faker('ru_RU')
fake.add_provider(Provider)


# асинхронная функция получения сообщения от сервера
async def receive_message(websocket):
    try:
        async for message in websocket:
            print(f"Получено сообщение от сервера: {message}")
    except websockets.ConnectionClosed:
        print("Соединение закрыто")


# асинхронная функция отправки сообщения на сервер
async def send_message():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Запуск корутины для получения сообщений от сервера
        receive_task = asyncio.create_task(receive_message(websocket))
        try:
            while True:
                sec = random.randint(1, 10)
                message = fake.name()
                await websocket.send(message)
                print(f"Отправлено сообщение серверу от клиента: У нас новый пользователь {message}, сгенери ему емейл")
                await asyncio.sleep(sec)  # Ожидание перед отправкой следующего сообщения
        except websockets.ConnectionClosed:
            print("Соединение закрыто")
        finally:
            receive_task.cancel()


if __name__ == "__main__":
    asyncio.run(send_message())


    
