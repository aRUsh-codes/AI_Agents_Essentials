import asyncio

"""
#Lock allows only one coroutine to access an object
lock = asyncio.Lock()
shared_resource = 0
async def modify_shared_resource():
    global shared_resource
    async with lock:
        #Critical section begins
        print(f"Resource before modification: {shared_resource}")
        shared_resource+=1
        await asyncio.sleep(1)
        print(f"Resource after modification: {shared_resource}")
        
async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))
"""

#Semaphore allows multiple coroutines to access the same object at the same time

async def acc(semaphore,id):
    async with semaphore:
        print(f"Accessing resource : f{id}")
        await asyncio.sleep(1)
        print(f"Releasing resource : f{id}")
        
async def main():
    semaphore = asyncio.Semaphore(2)
    await asyncio.gather(*(acc(semaphore,i) for i in range(5)))
    
asyncio.run(main())