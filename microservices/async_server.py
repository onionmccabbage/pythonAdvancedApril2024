import asyncio
from asyncio import StreamReader, StreamWriter

# be careful data-typing is development only (code hints) - it does NOT affect run-time
async def handle_echo(reader:StreamReader, writer:StreamWriter):
    data = await reader.read(1024) # this will be a byte string
    message = data.decode()
    addr = writer.get_extra_info('peername')
    # we may choose to usse __str__ or __repr__ for printed output
    # the default uses __str__ or we can say !s to force __str__
    # if we use !r it forces the print command to use __repr__ instead
    print(f'Received {message!r} from {addr!r}') # no end-of-line character
    print(f'Send message: {message!r}')
    writer.write(data)
    await writer.drain() # wait for the buffer to empty
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    # its recommended to use asyncio.run()
    asyncio.run(main())