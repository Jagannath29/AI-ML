import asyncio

async def fetch_data(id, sleep_time):
    print(f'Coroutine {id} starting to fetch data')

    await asyncio.sleep(sleep_time) # simulate a network request of i/o operatin

    return {"id": id, "data": f'sample data from coroutine{id}'}


async def main():
    # run coroutine concurrently and gather theri values
    result = await asyncio.gather(fetch_data(1,2), fetch_data(2,1), fetch_data(3,3))

    # process the result

    for r in result:
        print(f'Received result: {r}')


# run the main coroutine

asyncio.run(main())

# gather is not good at error handling
# it will not cancel automatically if any fetch_data fails