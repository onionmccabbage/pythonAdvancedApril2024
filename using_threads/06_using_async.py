# see https://docs.python.org/3/library/asyncio.html
import asyncio
import timeit

# we are obliged to use async and await together
async def main():
    '''just a normal function'''
    # when we await an outcome this will block the main thread
    await asyncio.sleep(1) # our long-running process
    print('hello')

if __name__ == '__main__':
    start = timeit.default_timer()
    # asyncio.run(  main() )
    # asyncio.run(  main() )
    # asyncio.run(  main() )
    # asyncio.run(  main() )
    # asyncio.run(  main() )
    with asyncio.Runner() as runner: # Runner is available in recent Python (3.12)
        runner.run(main())
        runner.run(main())
        runner.run(main())
        runner.run(main())
    end = timeit.default_timer()
    print(f'total time {end-start}')