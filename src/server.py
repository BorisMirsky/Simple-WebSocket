
import asyncio
import websockets
from faker import Faker                            # библиотекa генерации фейковых данных 
from faker.providers.person.ru_RU import Provider
import random

#назначаем порт на локалхосте
port = 1000

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
start_server = websockets.serve(handler, "localhost", port)

# запускаем сервер
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()




"""
async def handler(websocket):
    while True:
        try:
            message = await websocket.recv()
            print('Message received from client: ', message)
            await websocket.send("Message from server: " + message)
        except Exception as e:
            print(e)
            break

async def main():
    async with websockets.serve(handler, "", 8001):  # listen at port 8001
        await asyncio.Future()                       # run forever

if __name__ == "__main__":
    asyncio.run(main())

#############################


connected_clients = set()

async def handle_client(websocket, path):
    # Add the new client to the set of connected clients
    connected_clients.add(websocket)
    try:
        # Listen for messages from the client
        async for message in websocket:
            # Broadcast the message to all other connected clients
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        # Remove the client from the set of connected clients
        connected_clients.remove(websocket)

async def main():
    server = await websockets.serve(handle_client, 'localhost', 12345)
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())


"""
