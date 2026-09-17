import asyncio


async def task1():
    await asyncio.sleep(3)
    print("Task 1 completed")


async def task2():
    await asyncio.sleep(2)
    print("Task 2 completed")


# parllel calling
async def mai1():
    await asyncio.gather(
        task1(),
        task2()
    )

#sequential calling
async def main2():
    await task1()
    await task2()


asyncio.run(main2())