import asyncio

async def fetch_data(id, sleep_time):
    print(f'Coroutine {id} starting to fetch data.')

    await asyncio.sleep(sleep_time)
    return {'id': id, "data": f'Sample data from coroutine {id}'}


async def main():
    tasks = []

    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2,1,3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    # after task group block, all task are completed

    results = [task.result() for task in    tasks]


    for result in results:
        print(f'Result received: {result}')


asyncio.run(main())


# TaskkGroup provides builtin error handling if any of the task fails, this is more preferable