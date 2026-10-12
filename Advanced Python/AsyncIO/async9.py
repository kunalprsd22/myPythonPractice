
import asyncio


async def important_operation():
    await asyncio.sleep(2)
    print("Important operation completed")
    return "Saved"


async def main():
    task = asyncio.create_task(important_operation())

    try:
        result = await asyncio.wait_for(
            asyncio.shield(task),
            timeout=1
        )
        print(result)

    except TimeoutError:
        print("Caller timed out")

    # The inner task can still be running.
    result = await task
    print("Final result:", result)


asyncio.run(main())
