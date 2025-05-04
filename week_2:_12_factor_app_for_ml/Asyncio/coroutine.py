import asyncio



# define a coroutine that simulates a time consuming task

async def fetch_data(delay, id):

    print("Fetching data....id", id)
    
    await asyncio.sleep(delay) # simlate an i/o operation with a sleep

    print('Data fetched')
    print("Fetching data....id", id)

    return {"data": 'Some data', "id": id}

# another coroutine that calls a first coroutine 
async def main():

    # print("Start a main coroutine")

    task1 = fetch_data(2,1)
    task2 = fetch_data(2,2)

    # Await the fetch_data coroutine, pausing execution of main until fetch_data completes
    restult1 = await task1 # await to finish task 1
    print(f'Result received: {restult1}')

    restult2 = await task2 # await to finish task2
    print(f"Result Received: {restult2} ")

    # print('End of main coroutine ')
# run the main coroutine 
asyncio.run(main())

# print(main())

# Note: Coroutine doesn't start running wntil it is awaited