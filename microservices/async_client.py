import asyncio
import sys

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()   

    data = await reader.read(1024)
    print(f'Received: {data.decode()!r}')

    writer.close()
    await writer.wait_closed()

if __name__ == '__main__':
    message = ''
    if len(sys.argv) > 1:
        message += ' '.join(sys.argv[1:]) # combine system argument variables into a string
    asyncio.run(tcp_echo_client(message))