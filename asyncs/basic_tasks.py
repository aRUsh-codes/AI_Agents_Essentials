import asyncio

async def fetch_data(id,sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return {"id":id , "data":f"Sample data from coroutine {id}"}

async def main():
    #OPTION 1 Multiple singular tasks
    """task1 = asyncio.create_task(fetch_data(1,2))
    task2 = asyncio.create_task(fetch_data(2,3))
    task3 = asyncio.create_task(fetch_data(3,1))
    
    result1 = await task1
    result2 = await task2
    result3 = await task3
    
    print(result1,result2,result3)"""
    
    #OPTION 2 Gather function No builtin error handling and does not cancel out other tasks if one fails
    """results = await asyncio.gather(fetch_data(1,2),fetch_data(2,1),fetch_data(3,3))
    """
    
    #OPTION 3 TaskGroup builtin error handling and cancels out other tasks if one fails
    """tasks = []
    async with asyncio.TaskGroup() as tg:
        for i,sleep_time in enumerate([2,1,3],start=1):
            task = tg.create_task(fetch_data(i,sleep_time))
            tasks.append(task)
    
    results = [task.result() for task in tasks]
    
    for result in results:
        print(f"Recieved result : {result}")
    """
    
asyncio.run(main())