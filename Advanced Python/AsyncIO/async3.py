
import asyncio
import time


async def fetch_user():
    print("Fetching user...")
    await asyncio.sleep(2)
    print("User fetched")
    return {"id": 1, "name": "Jacky"}


async def fetch_orders():
    print("Fetching orders...")
    await asyncio.sleep(3)
    print("Orders fetched")
    return ["Order 101", "Order 102"]


async def main():
    start = time.perf_counter()

    # Schedule both operations
    user_task = asyncio.create_task(fetch_user())
    orders_task = asyncio.create_task(fetch_orders())

    print("Both tasks have been scheduled")

    # Wait for their results
    user = await user_task
    orders = await orders_task

    print("User:", user)
    print("Orders:", orders)
    print(f"Total time: {time.perf_counter() - start:.2f}s")


asyncio.run(main())
