
import asyncio
import websockets
from faker import Faker          # библиотекa генерации фейковых данных 
from faker.providers.person.ru_RU import Provider
import random
from websockets.asyncio.server import serve


#                 !!! for websockets version >= 15 !!!


#назначаем порт на локалхосте
port = 1000    # 8765
localhost = "127.0.0.1"
# создание объекта Faker с локализацией для России
fake = Faker('ru_RU')
fake.add_provider(Provider)

"""
# асинхронная функция
async def handler(websocket, path):
    try:
        async for message in websocket:
            op = random.randint(0, 100)
            print(f"Получено сообщение от клиента - новому пользователю {message} нужен email")
            if op > 10 :
                message_ser = fake.free_email()
                print(f"Отправлено клиенту для пользователя {message} сгенерирован email {message_ser}")
            else:
                message_ser = "сервер перегружен"
                print(f"Для пользователя {message} не удалось сгенерировать email, т.к. {message_ser}")
            await websocket.send(f"{message_ser}")
    except websockets.ConnectionClosed:
        print("Соединение закрыто")

# for 'websockets' version < 15
# объявляем сервер
#start_server = websockets.serve(handler, "localhost", port)
# запускаем сервер
#asyncio.get_event_loop().run_until_complete(start_server)
#asyncio.get_event_loop().run_forever()


# for 'websockets' version >= 15
async def main():
    async with websockets.serve(handler, "localhost", port):
        print("Server started on ws://localhost:1000")
        await asyncio.Future()  
"""

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)


async def main():
    async with serve(echo, localhost, port) as server:
        await server.serve_forever()

        
if __name__ == "__main__":
    asyncio.run(main())


