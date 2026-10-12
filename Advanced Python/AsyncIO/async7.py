
import asyncio


async def slow_operation():
    print("Operation started")
    await asyncio.sleep(10)
    return "Operation completed"


async def main():
    try:
        result = await asyncio.wait_for(
            slow_operation(),
            timeout=3
        )
        print(result)

    except TimeoutError:
        print("Operation timed out")


asyncio.run(main())
