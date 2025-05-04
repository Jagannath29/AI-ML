import asyncio

# variable
shared_resource = 0

# an asyncio lock
lock = asyncio.Lock()


async def modified_shared_resource():
    global shared_resource

    async with lock:

        # critical section starts
        print(f'Resources before modification: {shared_resource}')
        
        shared_resource += 1 # reso modified
        await asyncio.sleep(1) # simulate an io operation
        
        print(f'Resources after modification: {shared_resource}')

        # critical section ends


async def main():

    await asyncio.gather(*(modified_shared_resource() for _ in range(5)))
        


asyncio.run(main())
