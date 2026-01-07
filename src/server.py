
import asyncio
import websockets
from faker import Faker          # библиотекa генерации фейковых данных 
from faker.providers.person.ru_RU import Provider
import random


#назначаем порт на локалхосте
port = 1000    # 8765

# создание объекта Faker с локализацией для России
fake = Faker('ru_RU')
fake.add_provider(Provider)

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

# объявляем сервер
#start_server = websockets.serve(handler, "localhost", port)

# запускаем сервер
#asyncio.get_event_loop().run_until_complete(start_server)
#asyncio.get_event_loop().run_forever()
def start_server_sync():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    start_server = websockets.serve(handler, "localhost", port)
    loop.run_until_complete(start_server)
    loop.run_forever()

start_server_sync()
